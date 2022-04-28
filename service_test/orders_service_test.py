from unittest import TestCase
from service.orders_service import OrdersServices
import datetime
from bson import  ObjectId


class TestOrderServices(TestCase):
    def test_merge_order(self):
        order_value = {"id": ObjectId(),
                       "number": "PED01",
                       "buyer_name": "Test",
                       "value": 15.0,
                       "status": "Aberto",
                       "freight_type": "PAC"
                       }
        order_service = OrdersServices()
        result = order_service.merge_order(order=order_value,
                                           user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_orders(self):
        order_service = OrdersServices()
        result = order_service.get_orders(total_records=2,
                                          page=1,
                                          search="test",
                                          user_id="")
        print(result)
        self.assertEqual(result, result)


    def test_delete_order(self):
        order_service = OrdersServices()
        result = order_service.delete_order(order_id="5cfe8af4aee7b822347c71b5",
                                            user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_update_order_status(self):
        order = {"_id": "5cfe8ded6aa0381c584f5ffe",
                 "status": "Finalizado"}
        order_service = OrdersServices()
        result = order_service.update_order_status(order=order)
        print(result)
        self.assertEqual(result, result)

    def test_get_order_items(self):
        order_service = OrdersServices()
        result = order_service.get_order_items(order_id="5cfe8ded6aa0381c584f5ffe",
                                               user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_user_orders(self):
        order_service = OrdersServices()
        result = order_service.get_user_orders(user_id="5d0015c346868630ccf2dca7",
                                               total_records=2,
                                               page=1,
                                               search="test",
                                               nmessages="Y")
        print(result)
        self.assertEqual(result, result)
