import datetime
from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_DATE_MASK, C_INSERTING_ERROR, \
    C_GETTING_ERROR, C_UPDATING_ERROR, C_LOG_MESSAGE
from bson import ObjectId
from service.utils_service import success_to_json, error_to_json


class DatabaseVacationNotice(object):
    def __init__(self):
        pass

    def get_database_vacation_message(self, store_id, user_id):
        try:
            mc = MongoCollection()
            col = mc.vacation_notices()
            return col.find({"store_id": ObjectId(store_id), "user_id": ObjectId(user_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_vacation_message", "Getting", str(e), store_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_vacation_message(self, vacation_notice, user_id):
        arguments = ""
        try:
            arguments = vacation_notice
            mc = MongoCollection()
            col = mc.vacation_notices()
            dt = datetime.datetime.now()
            vacation_id = vacation_notice.get("id", None)
            result = col.update_one({"_id": ObjectId(vacation_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'date_range': vacation_notice['date_range'],
                                              'vacation_message': vacation_notice['vacation_message'],
                                              'vacation_receive_message': vacation_notice['vacation_receive_message'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    vacation_notice["creation_date"] = dt
                    vacation_notice["user_id"] = ObjectId(user_id)
                    r = col.insert_one(vacation_notice).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_vacation_message", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(vacation_notice['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_vacation_message", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
