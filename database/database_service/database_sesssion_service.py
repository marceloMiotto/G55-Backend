from database.database_setup.mongodb import MongoCollection
import datetime
from bson import ObjectId
from service.log_service import log_database
from constants import C_INSERTING_ERROR, C_LOG_MESSAGE
from service.utils_service import success_to_json, error_to_json


class DatabaseSessionService(object):
    def __init__(self):
        pass

    def get_database_session(self):
        try:
            mc = MongoCollection()
            col = mc.sessions()
            return col.insert_one({'createdAt': datetime.datetime.utcnow()}).inserted_id

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_session", "Getting", str(e), "Get All"))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))
