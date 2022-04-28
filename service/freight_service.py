from database.database_service.database_freight_service import DatabaseFreightTypeService
from service.page_pagination_service import PagePaginationService
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE
from bson.json_util import dumps, RELAXED_JSON_OPTIONS


class FreightServices(object):

    def __init__(self):
        pass

    def merge_freight_type(self, freight, user_id):
        try:
            freight_service = DatabaseFreightTypeService()
            result = freight_service.merge_database_freight_type(freight=freight,
                                                                 user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_freight_type", "Handling", str(e), freight))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_freight_type_count(self, search):
        try:
            freight = DatabaseFreightTypeService()
            result = freight.get_database_freight_count(search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_freight_type_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_freight_types(self, total_records, page, search, user_id):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search

            freight = DatabaseFreightTypeService()
            if total_records == 0:
                total_records = self.get_freight_type_count(search=search)

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

            result = freight.get_database_freight_types(search_word=search,
                                                        start=page,
                                                        user_id=user_id)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_freight_types", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_freight_type(self, freight_type_id, user_id):
        try:
            freight = DatabaseFreightTypeService()
            result = freight.delete_database_freight_types(freight_type_id=freight_type_id,
                                                           user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_freight_type", "Handling", str(e), freight_type_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
