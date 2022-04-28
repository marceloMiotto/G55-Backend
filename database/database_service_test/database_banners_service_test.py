from unittest import TestCase
from database.database_service.database_banners_service import DatabaseBannersService


class TestDatabaseBannersService(TestCase):
    def test_get_database_banners_front(self):
        service = DatabaseBannersService()
        store_id = "5d7bfc56f3150c2eb1a96d19"
        result = service.get_database_banners_front(store_id=store_id)
        for r in result:
            print(r)
        self.assertEqual(result, result)
