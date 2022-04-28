from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_INSERTING_ERROR, C_LOG_MESSAGE, C_DATE_MASK
from service.utils_service import success_to_json, error_to_json
import datetime


class DatabaseNewsletterService(object):
    def __init__(self):
        pass

    def post_database_newsletter_contact_front(self, newsletter):
        try:
            mc = MongoCollection()
            col = mc.newsletters()
            dt = datetime.datetime.now()
            r = col.insert_one({"email": newsletter["email"], "creation_date": dt}).inserted_id
            return success_to_json(str(r))

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_newsletter_contact_front", "Inserting", str(e), newsletter))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))
