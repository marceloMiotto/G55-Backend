from database.database_setup.mongodb import MongoCollection
from service.utils_service import success_to_json, error_to_json
from service.log_service import log_database
from constants import C_DATE_MASK, C_UPDATING_ERROR, C_INSERTING_ERROR, \
    C_GETTING_ERROR, C_LOG_MESSAGE
from bson import ObjectId
import datetime


class DatabaseAnalyticsService(object):
    def __init__(self):
        pass

    def get_database_analytics_flag(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.analytics()
            return col.find({"user_id": ObjectId(user_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_analytics_flag", "Getting", str(e), "Get All"))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_analytics(self, arguments, user_id):
        """
           Function to create or update the analytics flag
           Parameter: custom_analytics_flag - Y or N
           Return Error or Success
        """
        try:
            mc = MongoCollection()
            col = mc.analytics()
            dt = datetime.datetime.now()
            result = col.update_one({"user_id": ObjectId(user_id)},
                                    {'$set': {'analytics_flag': arguments['analytics_flag'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    arguments["creation_date"] = dt
                    arguments["user_id"] = ObjectId(user_id)
                    r = col.insert_one(arguments).inserted_id
                    return success_to_json(str(r))
                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_analytics", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(user_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_analytics", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
