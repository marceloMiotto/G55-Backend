from unittest import TestCase
from service.stores_service import StoresServices


class TestStoresServices(TestCase):


    def test_get_stores_front(self):
        store = StoresServices()
        result = store.get_stores_front(search_word="test", start=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_stores_front_one(self):
        store = StoresServices()
        result = store.get_store_front_one(store_code="plie_test")
        print(result)
        self.assertEqual(result, result)

    def test_get_user_store(self):
        stores = StoresServices()
        result = stores.get_user_store(user_id="5d656f9b1b05873050b793ff")
        print(result)
        self.assertEqual(result, result)

    def test_upsert_user_store(self):
        stores = StoresServices()
        store = {"name": "test service",
                 "description": "test test",
                 "user_id": "5c914cf378de470068b0d1d2"
                 }
        result = stores.upsert_user_store(content=store,
                                          user_id="")
        print(result)
        self.assertEqual(result, result)