from database.database_service.database_rating_service import DatabaseRatingService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class RatingServices(object):

    def __init__(self):
        pass

    def merge_rating(self, rating, user_id):
        try:
            rating_service = DatabaseRatingService()
            result = rating_service.merge_database_rating(rating=rating,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_rating", "Handling", str(e), rating))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_ratings_count(self, ref_id):
        try:
            rating_service = DatabaseRatingService()
            result = rating_service.get_database_ratings_count(ref_id=ref_id)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_ratings_count", "Handling", str(e), ref_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_ratings(self, total_records, page, ref_id):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - ref_id: " + ref_id
            rating_service = DatabaseRatingService()
            if total_records == 0:
                total_records = self.get_ratings_count(ref_id=ref_id)

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

            result = rating_service.get_database_ratings(ref_id=ref_id,
                                                         start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_ratings", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_rating(self, rating_id, user_id):
        try:
            rating_service = DatabaseRatingService()
            result = rating_service.delete_database_rating(rating_id=rating_id,
                                                           user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_rating", "Handling", str(e), rating_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def update_rating_review(self, rating_id, rating):
        arguments = ""
        try:
            arguments = "rating_id: " + rating_id + " rating: " + str(rating)
            rating_service = DatabaseRatingService()
            result = rating_service.update_database_rating_answer(rating_id=rating_id,
                                                                  rating=rating)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("update_rating_review", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)