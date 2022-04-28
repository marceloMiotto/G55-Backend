from database.database_service.database_vacation_message_service import DatabaseVacationNotice
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE
from service.log_service import log
from service.utils_service import error_to_json


class VacationNoticeServices(object):

    def __init__(self):
        pass

    def merge_vacation_message(self, vacation_notice, user_id):
        try:
            database_vacation = DatabaseVacationNotice()
            result = database_vacation.merge_database_vacation_message(vacation_notice=vacation_notice,
                                                                       user_id=user_id)

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_vacation_message", "Handling", str(e), vacation_notice))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_vacation_message(self, store_id, user_id):
        try:
            database_vacation = DatabaseVacationNotice()
            result = database_vacation.get_database_vacation_message(store_id=store_id,
                                                                     user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_vacation_message_obj", "Handling", str(e), store_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

