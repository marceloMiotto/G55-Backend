from database.database_service.database_coupon_service import DatabaseCouponService
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE
import random
from service.page_pagination_service import PagePaginationService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS


class CouponServices(object):

    def __init__(self):
        pass
        # TODO review docs for each function on the system

    def get_coupon_count(self, user_id, search):
        try:
            coupon = DatabaseCouponService()
            result = coupon.get_database_coupon_count(user_id=user_id,
                                                      search=search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_coupon_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_automatic_coupon_code(self):
        """
           Function to create the new automatic coupon code
        """
        try:
            # TODO define a random code however unique
            code = ''.join(random.choice('0123456789ABCDEFGHIJLMNOPQRSTUVXZ') for i in range(16))
            print(code)
            code += "#"
            return code

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_automatic_coupon", "Handling", str(e), "Get automatic coupon code"))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_coupon(self, coupon, user_id):
        """ This function must merge all values for coupons
            Coupon
        """
        try:
            coupon_service = DatabaseCouponService()
            result = coupon_service.merge_database_coupon(coupon,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_coupon", "Handling", str(e), coupon))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_coupon(self, coupon_id, user_id):
        """ This function must get all values for coupon """
        try:
            coupon_service = DatabaseCouponService()
            result = coupon_service.get_database_coupon(coupon_id=coupon_id,
                                                        user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_coupon", "Handling", str(e), coupon_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_coupon(self, coupon_id, user_id):
        """ The deletion will be in cascade
        """
        try:
            coupon_service = DatabaseCouponService()
            result = coupon_service.delete_database_coupon(coupon_id=coupon_id,
                                                           user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_coupon", "Handling", str(e), coupon_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_coupons(self, user_id, total_records, page, search):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " total_records: " + str(total_records) + \
                        " - page: " + str(page) + " - search: " + search
            coupon = DatabaseCouponService()
            if total_records == 0:
                total_records = self.get_coupon_count(user_id=user_id, search=search)

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

            result = coupon.get_database_coupons(user_id=user_id,
                                                 search_word=search,
                                                 start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_coupons", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_coupon_enable_disable(self, coupon, user_id):
        try:
            coupon_service = DatabaseCouponService()
            result = coupon_service.post_database_coupon_enable_disable(coupon=coupon,
                                                                        user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_coupon_enable_disable", "Handling", str(e), coupon))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def coupon_cancel(self, coupon, user_id):
        try:
            coupon_service = DatabaseCouponService()
            result = coupon_service.cancel_database_coupon(coupon=coupon,
                                                           user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("coupon_cancel", "Handling", str(e), coupon))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
