from unittest import TestCase
from database.database_service.database_stores_service import DatabaseStoresService
import datetime

class TestDatabaseCartService(TestCase):

    def test_get_database_user_cart_front(self):
        stores = DatabaseStoresService()
        result = stores.get_database_stores_front()
        print(result)
        self.assertEqual(result, result)

    def test_get_database_fav_stores_front(self):
        stores = DatabaseStoresService()
        result = stores.get_database_fav_stores_front(user_id=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_stores_front(self):
        stores = DatabaseStoresService()
        result = stores.get_database_stores_front(search_word="test",
                                                  start=1)
        for r in result:
            print(r)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_store_front_one(self):
        stores = DatabaseStoresService()
        result = stores.get_database_store_front_one(store_code="plie_test")
        for r in result:
            print(r)
        print(result)
        self.assertEqual(result, result)

    def test_is_store_code_unique(self):
        stores = DatabaseStoresService()
        result = stores.is_store_code_unique(store_code="mar")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_store_id(self):
        stores = DatabaseStoresService()
        result = stores.get_database_store_id(store_code="plie_test")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_user_store(self):
        stores = DatabaseStoresService()
        result = stores.get_database_user_store(user_id="5d656f9b1b05873050b793ff")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_user_store(self):
        stores = DatabaseStoresService()
        store = {"name": "test",
                 "description": "test test",
                 "user_id": "123450"
                 }
        result = stores.merge_database_user_store(store=store)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_google_analytics_code(self):
        analytics = DatabaseStoresService()
        analytics_object = analytics.get_database_google_analytics_code(user_id="5cec370caee7b8360c111bb2")
        print(analytics_object)
        for r in analytics_object:
            print(r)
        self.assertEqual(analytics_object, analytics_object)

    def test_update_database_google_analytics_code(self):
        analytics_obj = {"_id": "",
                         "google_analytics_code": "123",
                         "user_id": "123",
                         "creation_date": str(datetime.datetime.now()),
                         "last_updated_date": str(datetime.datetime.now())
                         }
        analytics = DatabaseStoresService()
        result = analytics.merge_database_google_analytics_code(arguments=analytics_obj)
        print(result)
        self.assertEqual(result, result)