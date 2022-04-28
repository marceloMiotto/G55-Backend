from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_GETTING_ERROR, C_LOG_MESSAGE
from service.utils_service import success_to_json, error_to_json
from bson.json_util import ObjectId


class DatabaseBannersService(object):
    def __init__(self):
        pass

    def get_database_banners_front(self, store_id):
        try:
            mc = MongoCollection()
            col = mc.banners()
            return col.find({'store_id': ObjectId(store_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_banners_front", "Getting", str(e), str(store_id)))
            return error_to_json(C_GETTING_ERROR.format(str(e)))
