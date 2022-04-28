from database.database_service.database_messages_service import DatabaseMessageService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR


class MessageServices(object):

    def __init__(self):
        pass

    def get_messages(self, customer_profile_id, store_id):
        arguments = ""
        try:
            arguments = "customer_profile_id: " + customer_profile_id + "store_id: " + store_id
            database_messages = DatabaseMessageService()
            result = database_messages.get_database_messages(customer_profile_id=customer_profile_id,
                                                             store_id=store_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_messages", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_message(self, message, user_id):
        try:
            database_messages = DatabaseMessageService()
            result = database_messages.post_database_message(message=message,
                                                             user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_message_front", "Handling", str(e), message))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_messages_user_session(self, contact_id):
        try:
            database_messages = DatabaseMessageService()
            result = database_messages.get_database_messages_session(contact_id=contact_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_messages_session", "Handling", str(e), contact_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def merge_messages_session(self, message_session):
        try:
            database_messages = DatabaseMessageService()
            result = database_messages.merge_database_messages_session(message_session=message_session)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_messages_session", "Handling", str(e), message_session))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)