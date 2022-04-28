from database.database_service.database_orders_service import DatabaseOrdersService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class OrdersServices(object):

    def __init__(self):
        pass

    def update_order_status(self, order):
        try:
            order_service = DatabaseOrdersService()
            result = order_service.update_database_order_status(order=order)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("update_order_status", "Handling", str(e), order))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def merge_order(self, order, user_id):
        try:
            order_service = DatabaseOrdersService()
            result = order_service.merge_database_order(order=order,
                                                        user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_order", "Handling", str(e), order))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_orders_count(self, user_id, search, json_filter):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " search: " + search
            order_service = DatabaseOrdersService()
            result = order_service.get_database_orders_count(user_id=user_id,
                                                             search=search,
                                                             json_filter=json_filter)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_orders_count", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_orders(self, user_id, total_records, page, search, json_filter):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search
            order_service = DatabaseOrdersService()
            if total_records == 0:
                total_records = self.get_orders_count(user_id=user_id,
                                                      search=search,
                                                      json_filter=json_filter)

            pagination_service = PagePaginationService(total_records=total_records, page=page)

            print("debug1")

            if total_records == 0:
                result_header = pagination_service.serialize
                return result_header

            stop_limit = pagination_service.get_higher_limit()

            if stop_limit >= total_records:
                stop_limit = total_records

            start_limit = pagination_service.get_lower_limit() - 1

            if start_limit >= stop_limit:
                return None

            print("debug2")

            result = order_service.get_database_orders(user_id=user_id,
                                                       search_word=search,
                                                       start=page,
                                                       json_filter=json_filter)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            print("debug5")

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_orders", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_order(self, order_id, user_id):
        try:
            order_service = DatabaseOrdersService()
            result = order_service.delete_database_order(order_id=order_id,
                                                         user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_order", "Handling", str(e), order_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_order_items(self, order_id, user_id):
        try:
            order_service = DatabaseOrdersService()
            result = order_service.get_database_order_items(order_id=order_id,
                                                            user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_order_items", "Handling", str(e), order_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_user_orders_count(self, user_id, search, nmessages):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " search: " + search
            order_service = DatabaseOrdersService()
            result = order_service.get_database_user_orders_count(user_id=user_id,
                                                                  search=search,
                                                                  nmessages=nmessages)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_user_orders_count", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_user_orders(self, user_id, total_records, page, search, nmessages):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search + " nmessages: " + nmessages
            order_service = DatabaseOrdersService()
            if total_records == 0:
                total_records = self.get_user_orders_count(user_id=user_id,
                                                           search=search,
                                                           nmessages=nmessages)

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

            result = order_service.get_database_user_orders(user_id=user_id,
                                                            search_word=search,
                                                            start=page,
                                                            nmessages=nmessages)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_user_orders", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)




