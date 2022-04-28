from database.database_service.database_analytics_service import DatabaseAnalyticsService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.log_service import log
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.utils_service import error_to_json


class AnalyticsServices(object):

    def __init__(self):
        pass

    def merge_analytics(self, custom_analytics, user_id):
        try:
            database_analytics = DatabaseAnalyticsService()
            result = database_analytics.merge_database_analytics(arguments=custom_analytics,
                                                                 user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_google_analytics_code", "Handling", str(e), custom_analytics))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_analytics_flag(self, user_id):
        try:
            database_analytics = DatabaseAnalyticsService()
            result = database_analytics.get_database_analytics_flag(user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_custom_analytics", "Handling", str(e), "Get All"))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
