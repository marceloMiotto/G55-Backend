from database.database_service.database_standard_message_service import DatabaseStandardMessageService
from service.page_pagination_service import PagePaginationService
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE
from bson.json_util import dumps, RELAXED_JSON_OPTIONS


class StandardMessageService(object):

    def __init__(self):
        pass

    def merge_standard_message(self, smessage, user_id):
        try:
            messages = DatabaseStandardMessageService()
            result = messages.merge_database_standard_message(smessage=smessage,
                                                              user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_standard_message", "Handling", str(e), smessage))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_standard_messages_count(self, user_id, search):
        try:
            messages = DatabaseStandardMessageService()
            result = messages.get_database_standard_message_count(user_id=user_id,
                                                                  search=search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_standard_messages_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_standard_messages(self, user_id, total_records,  page, search):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + "total_records: " + str(total_records) + \
                        " - page: " + str(page) + " - search: " + search
            messages = DatabaseStandardMessageService()
            if total_records == 0:
                total_records = self.get_standard_messages_count(user_id=user_id,
                                                                 search=search)

            pagination_service = PagePaginationService(total_records=total_records, page=page)

            if total_records == 0:
                result_header = pagination_service.serialize
                return result_header

            stop_limit = pagination_service.get_higher_limit()
            if stop_limit >= total_records:
                stop_limit = total_records

            start_limit = pagination_service.get_lower_limit() - 1

            if start_limit >= stop_limit:
                return None

            result = messages.get_database_standard_messages(user_id=user_id,
                                                             search_word=search,
                                                             start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_standard_messages", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_standard_message(self, message_id, user_id):
        try:
            messages = DatabaseStandardMessageService()
            result = messages.delete_database_standard_messages(message_id=message_id,
                                                                user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_standard_message", "Handling", str(e), message_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)


