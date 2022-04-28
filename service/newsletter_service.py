from database.database_service.database_newsletter_service import DatabaseNewsletterService
from bson.json_util import dumps
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR
from service.log_service import log
from service.utils_service import error_to_json


class NewsletterServices(object):

    def __init__(self):
        pass

    def post_newsletter_contact_front(self, newsletter):
        try:
            database_news = DatabaseNewsletterService()
            result = database_news.post_database_newsletter_contact_front(newsletter=newsletter)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_newsletter_contact_front", "Handling", str(e), newsletter))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))
