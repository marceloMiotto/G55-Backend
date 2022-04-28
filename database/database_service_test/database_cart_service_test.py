from unittest import TestCase
from database.database_service.database_cart_service import DatabaseCartService
from bson.json_util import dumps
from bson import ObjectId


class TestDatabaseCartService(TestCase):

    def test_update_database_store_coupon_product_cart(self):
        user_cart = DatabaseCartService()
        result = user_cart.update_database_store_coupon_product_cart(cart_id="5ccb1b5faee7b844e89368d2",
                                                                     product_id="5cae2a740b71272b40e3ae46",
                                                                     discount=1.6)
        self.assertEqual(result, result)

    def test_update_database_store_coupon_cart(self):
        user_cart = DatabaseCartService()
        result = user_cart.update_database_store_coupon_cart(cart_id="5ccb1b5faee7b844e89368d2",
                                                             coupon_code="DESC123",
                                                             coupon_discount=12.6)
        self.assertEqual(result, result)

    def test_get_database_user_store_cart_front(self):
        user_cart = DatabaseCartService()
        find_statement = {'$and': [{'user_id': ObjectId('5ccb1b01aee7b844e89368d0')},
                                   {'store_id': ObjectId('5ccb1c22e57f8f3de812db45')},
                                   {'products.product_name': {'$nin': ["test", "Test 2"]}},
                                   {'products.category_name': {'$nin': ["Bis", "Test 2"]}}
                                   ]
                          }
        result = user_cart.get_database_user_store_cart_front(find_statement=find_statement)
        print(dumps(result))
        self.assertEqual(result, result)

    def test_get_database_cart_coupon_front(self):
        user_cart = DatabaseCartService()
        result = user_cart.get_database_coupon_front(coupon_code="DESC123",
                                                     store_id="5ccb1c22e57f8f3de812db45")
        print(dumps(result))
        self.assertEqual(result, result)

    def test_post_database_cart_product_observation_front(self):
        product = {"cart_id": "5cc762b4aee7b8038cd4250a",
                   "product_id": "5c991bd0eae4fc0f1cb5f2c0",
                   "observations": "test 2 "
                   }
        user_cart = DatabaseCartService()
        result = user_cart.post_database_cart_product_observation_front(product)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_user_cart(self):
        user_cart = DatabaseCartService()
        result = user_cart.get_database_user_cart(user_id="5cc33c9eaee7b816c8a30ef7")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_post_database_cart_product_gift_front(self):
        product = {"cart_id": "5cc71b3aaee7b839c40bc039",
                   "product_id": "5cae2a740b71272b40e3ae46",
                   "gift_flag": "N"
                   }
        user_cart = DatabaseCartService()
        result = user_cart.post_database_cart_product_gift_front(product)
        print(result)
        self.assertEqual(result, result)

    def test_post_database_cart_product_quantity_front(self):
        product = {"cart_id": "5cc0c559aee7b841348d116f",
                   "product_id": "5cae2a740b71272b40e3ae46",
                   "quantity": 2
                   }
        user_cart = DatabaseCartService()
        result = user_cart.post_database_cart_product_quantity_front(product)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_user_cart_front(self):
        user_cart = DatabaseCartService()
        result = user_cart.get_database_user_cart_front(user_id="5c914cf378de470068b0d1d2")
        print(result)
        self.assertEqual(result, result)

    def test_post_database_user_cart_front(self):
        product = {"user_id": "5cc33c9eaee7b816c8a30ef7",
                   "store_id": "5c994c25eae4fc0f1cb5f2c3",
                   "store_code": "Plie",
                   "product_id": "5caf53646eeb6210b46ef4f2",
                   "quantity": 1,
                   "product_name": "Product Test 4",
                   "product_photo": 4,
                   "price": 2.5,
                   "gift_value": 1,
                   "gift_flag": "Y",
                   "observations": "",
                   "freight_value": 0,
                   "freight_type": "",
                   "freight_eta": 0, "coupon": ""}

        user_cart = DatabaseCartService()
        result = user_cart.post_database_user_cart_front(product=product)
        self.assertEqual(result, result)


def test_delete_database_user_cart_product_front(self):
    user_cart = DatabaseCartService()
    result = user_cart.delete_database_user_cart_product_front(user_id="5c914cf378de470068b0d1d2",
                                                               store_id="5c8c003feaa994293038e8b9",
                                                               product_id="5c8c003feaa994293038e8b8",
                                                               quantity=2)
    print(result)
    self.assertEqual(result, result)


def test_delete_database_user_cart_store_front(self):
    user_cart = DatabaseCartService()
    result = user_cart.delete_database_user_cart_store_front(user_id="5c914cf378de470068b0d1d2",
                                                             store_id="5c8c003feaa994293038e8b9")

    print(result)
    self.assertEqual(result, result)
