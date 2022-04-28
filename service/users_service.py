from database.database_service.database_users_service import DatabaseUsersService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, ObjectId
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR, C_SUCCESS, C_NOT_ALLOWED
from service.log_service import log
from service.utils_service import error_to_json, success_to_json
from service.token_service import CodeServices


class UsersServices(object):

    def __init__(self):
        pass

    def create_user_account(self, user):
        try:
            token = ""
            result = self.user_exists(user["email"])
            if int(result) > 0:
                return dumps(error_to_json(C_HANDLE_ERROR.format("User exists")), json_options=RELAXED_JSON_OPTIONS)

            else:

                result = self.merge_user(user=user, user_id=None)

                if result.find(C_SUCCESS) > 0:
                    tokens_service = CodeServices()
                    user_info = self.get_user_info(user_code=user["email"])
                    for u in user_info:
                        token = tokens_service.token_encode(u)
                else:
                    raise ValueError

                return token

        except Exception as e:
            log(C_LOG_MESSAGE.format("create_user_account", "Handling", str(e), user))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def merge_user(self, user, user_id=None):
        try:
            user_service = DatabaseUsersService()
            result = user_service.merge_database_user(user=user,
                                                      user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_user", "Handling", str(e), str(user)))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_users_count(self, search):
        try:
            user_service = DatabaseUsersService()
            result = user_service.get_database_users_count(search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_users_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_users(self, total_records, page, search):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search
            user_service = DatabaseUsersService()
            if total_records == 0:
                total_records = self.get_users_count(search=search)

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

            result = user_service.get_database_users(search_word=search,
                                                     start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_users", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_user(self, user_code):
        try:
            user_service = DatabaseUsersService()
            result = user_service.delete_database_user(user_code=user_code)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_category", "Handling", str(e), user_code))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_user_enable_disable(self, user):
        try:
            user_service = DatabaseUsersService()
            result = user_service.post_database_user_enable_disable(user=user)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_user_enable_disable", "Handling", str(e), user))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def authenticate_user(self, user):
        try:

            #  TODO verify how to handle when there is no user
            user_service = DatabaseUsersService()
            result = user_service.verify_database_user_credentials(user)
            token = ""

            if type(result) == str:
                return dumps(result)
            else:
                for re in result:
                    tokens_service = CodeServices()
                    token = tokens_service.token_encode(re)
                    print(token)

                if not token:
                    return dumps(error_to_json(C_HANDLE_ERROR.format(C_NOT_ALLOWED)), json_options=RELAXED_JSON_OPTIONS)

                return success_to_json(token)

        except Exception as e:
            log(C_LOG_MESSAGE.format("authenticated_user", "Handling", str(e), user))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_user_info(self, user_code):
        arguments = ""
        try:
            arguments = "user_code: " + user_code
            user_service = DatabaseUsersService()
            result = user_service.get_database_user_info(user_code=user_code)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_user_info", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def user_exists(self, user_code):
        arguments = ""
        try:
            arguments = "user_code: " + user_code
            user_service = DatabaseUsersService()
            result = user_service.user_database_exists(user_code=user_code)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("user_exists", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

