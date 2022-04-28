from unittest import TestCase
from database.database_service.database_newsletter_service import DatabaseNewsletterService


class TestNewsletterServices(TestCase):

    def test_get_banners_front(self):
        json_news = {"email": "Test3"}
        news = DatabaseNewsletterService()
        result = news.post_database_newsletter_contact_front(newsletter=json_news)
        print(result)
        self.assertEqual(result, result)
