from database.database_service.database_complaint_service import DatabaseComplaintService
from service.page_pagination_service import PagePaginationService
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from constants import C_HANDLE_ERROR, C_LOG_MESSAGE
from service.log_service import log
from service.utils_service import error_to_json


class ComplaintServices(object):

    def __init__(self):
        pass

    def insert_complaint(self, complaint, user_id):
        try:
            database_complaint = DatabaseComplaintService()
            result = database_complaint.insert_database_complaint(complaint=complaint,
                                                                  user_id=user_id)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("insert_complaint", "Handling", str(e), complaint))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_complaints_count(self, search):
        try:
            comps = DatabaseComplaintService()
            result = comps.get_database_complaints_count(search_word=search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_complaints_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_complaint(self, complaint_id):
        try:
            comps = DatabaseComplaintService()
            result = comps.get_database_complaint(complaint_id)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_complaint", "Handling", str(e), complaint_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_complaints(self, total_records, page, search):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search

            comps = DatabaseComplaintService()
            if total_records == 0:
                total_records = self.get_complaints_count(search=search)

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

            result = comps.get_database_complaints(search_word=search,
                                                   start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_complaints", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_complaint(self, complaint_id):
        try:
            comps = DatabaseComplaintService()
            result = comps.delete_database_complaint(complaint_id=complaint_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_complaint", "Handling", str(e), complaint_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
