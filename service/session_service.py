from database.database_service.database_sesssion_service import DatabaseSessionService
from bson.json_util import dumps
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE


class SessionServices(object):

    def __init__(self):
        pass

    def get_session(self):
        try:
            database_service = DatabaseSessionService()
            result = database_service.get_database_session()
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_session", "Handling", str(e), "Get Service ID"))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))
