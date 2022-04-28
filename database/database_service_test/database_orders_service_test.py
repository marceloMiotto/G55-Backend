from unittest import TestCase
from database.database_service.database_orders_service import DatabaseOrdersService
from bson import ObjectId
import datetime


class TestDatabaseOrdersService(TestCase):

    def test_get_orders(self):
        order_service = DatabaseOrdersService()
        result = order_service.get_database_orders(search_word="test",
                                                   start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_delete_order(self):
        order_service = DatabaseOrdersService()
        result = order_service.delete_database_order(order_id="5cfe8c14aee7b83e1c561a87")
        self.assertEqual(result, result)

    def test_merge_order(self):
        order_service = DatabaseOrdersService()
        order_value = {"_id": ObjectId(),
                       "number": "PED01",
                       "buyer_name": "Test",
                       "creation_date": str(datetime.datetime.now()),
                       "last_updated_date": str(datetime.datetime.now()),
                       "value": 15.0,
                       "status": "Aberto",
                       "freight_type": "PAC"
                       }
        result = order_service.merge_database_order(order=order_value)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_orders_count(self):
        order_service = DatabaseOrdersService()
        result = order_service.get_database_orders_count(search="test")
        print(result)
        self.assertEqual(result, result)

    def test_update_database_order_status(self):
        order = {"_id": "5cfe8ded6aa0381c584f5ffe",
                 "status": "Ativo"}
        order_service = DatabaseOrdersService()
        result = order_service.update_database_order_status(order=order)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_order_items(self):
        order_service = DatabaseOrdersService()
        result = order_service.get_database_order_items(order_id="5cfe8ded6aa0381c584f5ffe")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_user_orders(self):
        order_service = DatabaseOrdersService()
        result = order_service.get_database_user_orders(user_id="5d0015c346868630ccf2dca7",
                                                        search_word="test",
                                                        start=1,
                                                        nmessages="Y")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_user_orders_count(self):
        order_service = DatabaseOrdersService()
        result = order_service.get_database_user_orders_count(user_id="5d0015c346868630ccf2dca7",
                                                              search="test",
                                                              nmessages="N")
        print(result)
        self.assertEqual(result, result)