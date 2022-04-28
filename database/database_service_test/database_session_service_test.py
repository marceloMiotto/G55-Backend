from unittest import TestCase
from database.database_service.database_sesssion_service import DatabaseSessionService


class TestDatabaseSessionService(TestCase):
    def test_get_database_service(self):
        service = DatabaseSessionService()
        result = service.get_database_session()
        print(result)
        self.assertEqual(result, result)
