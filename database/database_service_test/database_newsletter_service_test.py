from unittest import TestCase
from database.database_service.database_newsletter_service import DatabaseNewsletterService


class TestDatabaseNewsletterService(TestCase):

    def test_post_database_newsletter_contact_front(self):

        newsletter = {"email": "test2"}
        news = DatabaseNewsletterService()
        result = news.post_database_newsletter_contact_front(newsletter=newsletter)
        self.assertEqual(result, result)
