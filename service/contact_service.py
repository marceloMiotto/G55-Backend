from database.database_service.database_contact_service import DatabaseContactService
from bson.json_util import dumps
from service.page_pagination_service import PagePaginationService
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class ContactServices(object):

    def __init__(self):
        pass

    def insert_contact(self, contact):
        try:
            contact_service = DatabaseContactService()
            result = contact_service.insert_database_contact(contact=contact)
            return dumps(result)


        except Exception as e:
            log(C_LOG_MESSAGE.format("insert_contact", "Handling", str(e), contact))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def upsert_contact(self, contact):
        try:
            contact_service = DatabaseContactService()
            result = contact_service.upsert_database_contact_answer(contact=contact)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("upsert_contact", "Handling", str(e), contact))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_contacts_count(self, search):
        try:
            contact = DatabaseContactService()
            result = contact.get_database_contacts_count(search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_contacts_count", "Handling", str(e), search))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_contacts(self, total_records, page, search):
        arguments = ""
        try:
            arguments = "total_records: " + str(total_records) + " - page: " + str(page) + \
                        " - search: " + search

            contact = DatabaseContactService()
            if total_records == 0:
                total_records = self.get_contacts_count(search=search)

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

            result = contact.get_database_contacts(search_word=search,
                                                   start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_contacts", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def delete_contact(self, contact_id):
        try:
            contact_service = DatabaseContactService()
            result = contact_service.delete_database_contact(contact_id=contact_id)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_contact", "Handling", str(e), contact_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))


