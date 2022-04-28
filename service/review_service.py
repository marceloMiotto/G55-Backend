from database.database_service.database_review_service import DatabaseReviewsService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class ReviewServices(object):

    def __init__(self):
        pass

    def get_reviews_front(self, ref_id):
        try:
            database_reviews = DatabaseReviewsService()
            result = database_reviews.get_database_reviews_front(ref_id=ref_id)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_reviews_front", "Handling", str(e), ref_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def insert_review(self, review, user_id):
        try:
            service = DatabaseReviewsService()
            result = service.insert_database_review(review=review,
                                                    user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("insert_review", "Handling", str(e), review))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_reviews_count(self, user_id, search):
        try:
            service = DatabaseReviewsService()
            result = service.get_database_reviews_count(user_id=user_id, search_word=search)
            return result
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_reviews_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_reviews(self, user_id, total_records, page, search):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + "total_records: " + str(total_records) + \
                        "page: " + str(page) + \
                        "search: " + search
            service = DatabaseReviewsService()
            if total_records == 0:
                total_records = self.get_reviews_count(user_id=user_id, search=search)

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

            result = service.get_database_reviews(user_id=user_id,
                                                  search_word=search,
                                                  start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_reviews", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_review(self, review_id, user_id):
        try:
            service = DatabaseReviewsService()
            result = service.delete_database_review(review_id=review_id,
                                                    user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_review", "Handling", str(e), review_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
