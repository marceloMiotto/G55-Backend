from database.database_service.database_banners_service import DatabaseBannersService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.utils_service import error_to_json
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log


class BannersServices(object):

    def __init__(self):
        pass

    def get_banners_front(self, store_id):
        try:
            database_banners = DatabaseBannersService()
            result = database_banners.get_database_banners_front(store_id=store_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_banners_front", "Handling", str(e), "store_id: " + str(store_id)))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
