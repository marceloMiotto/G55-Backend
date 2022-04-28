from database.database_service.database_stores_service import DatabaseStoresService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR, C_SUCCESS
from service.log_service import log
from service.utils_service import error_to_json
from service.directory_service import DirectoryService
import ast

#  TODO verify where to validate the unique store_code


class StoresServices(object):

    def __init__(self):
        pass

    def get_store_front_one(self, store_code):
        arguments = ""
        try:
            arguments = "store_code: " + store_code
            stores = DatabaseStoresService()
            result = stores.get_database_store_front_one(store_code=store_code)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_store_front_one", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_stores_front(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            stores = DatabaseStoresService()
            result = stores.get_database_stores_front(search_word=search_word, start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_stores_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_store_id(self, store_code):
        arguments = ""
        try:
            arguments = "store_name: " + store_code
            stores = DatabaseStoresService()
            result = stores.get_database_store_id(store_code=store_code)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_store_id", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_user_store(self, user_id):
        arguments = ""
        try:
            arguments = "user_id: " + user_id
            stores = DatabaseStoresService()
            result = stores.get_database_user_store(user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_user_store", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def upsert_user_store(self, content, user_id):
        arguments = ""
        try:
            arguments = "content: " + str(content)
            stores = DatabaseStoresService()
            result = stores.merge_database_user_store(store=content,
                                                      user_id=user_id)
            dic_result = ast.literal_eval(result)
            print(type(dic_result))

            if dic_result["result"] == C_SUCCESS:
                directory_service = DirectoryService()
                directory_service.create_directories(store_id=dic_result["id"])

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("upsert_user_store", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def update_google_analytics_code(self, analytics, user_id):
        try:
            database_analytics = DatabaseStoresService()
            result = database_analytics.update_database_google_analytics_code(arguments=analytics,
                                                                              user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_google_analytics_code", "Handling", str(e), analytics))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_google_analytics_code(self, user_id):
        try:
            database_analytics = DatabaseStoresService()
            result = database_analytics.get_database_google_analytics_code(user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_google_analytics_code", "Handling", str(e), "Get google analytics code"))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
