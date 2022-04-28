from database.database_service.database_category_service import DatabaseCategoryService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class CategoryServices(object):

    def __init__(self):
        pass

    def get_categories_front(self, store_id, store_code):
        arguments = "store_id: " + str(store_id) + " - store_code: " + store_code
        try:
            category = DatabaseCategoryService()
            result = category.get_database_categories_front(store_id=store_id, store_code=store_code)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_categories_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def merge_category(self, category, user_id):
        try:
            category_service = DatabaseCategoryService()
            result = category_service.merge_database_category(category=category,
                                                              user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_category", "Handling", str(e), category))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_category_count(self, search):
        try:
            category = DatabaseCategoryService()
            result = category.get_database_category_count(search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_category_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_categories(self, total_records, page, search, user_id):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search
            category = DatabaseCategoryService()
            if total_records == 0:
                total_records = self.get_category_count(search=search)

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

            result = category.get_database_categories(search_word=search,
                                                      start=page,
                                                      user_id=user_id)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_categories", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_category(self, category_id, user_id):
        try:
            category = DatabaseCategoryService()
            result = category.delete_database_category(category_id=category_id,
                                                       user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_category", "Handling", str(e), category_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_category_id(self, category_name):
        try:
            category = DatabaseCategoryService()
            result = category.get_database_category_id(category_name=category_name)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_category", "Handling", str(e), category_name))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)