from unittest import TestCase
from service.cart_service import CartServices


class TestCartServices(TestCase):

    def test_post_reset_user_cart_coupon(self):
        cart = CartServices()
        result = cart.post_reset_user_cart_coupon(user_id="5ccc93d7aee7b8483414f1dc")
        print(result)
        self.assertEqual(result, result)

    def test_post_cart_coupon_front(self):
        product = {"cart_id": "5ccb1b5faee7b844e89368d2",
                   "store_id": "5ccb1c22e57f8f3de812db45",
                   "user_id": "5ccb1b01aee7b844e89368d0",
                   "coupon_code": "DESC123"
                   }

        cart = CartServices()
        result = cart.post_cart_coupon_front(product=product)
        print(result)
        self.assertEqual(result, result)

    def test_post_cart_product_observation_front(self):
        product = {"cart_id": "5cc76592aee7b84128d5cfb2",
                   "product_id": "5c991bd0eae4fc0f1cb5f2c0",
                   "observations": "G 1"
                   }
        cart = CartServices()
        result = cart.post_cart_product_observation_front(product=product)
        print(result)
        self.assertEqual(result, result)


    def test_post_cart_product_gift_front(self):
        product = {"cart_id": "5cc71b3aaee7b839c40bc039",
                   "product_id": "5cae2a740b71272b40e3ae46",
                   "gift_flag": "G",
                   "user_id": "5cc71a04aee7b839c40bc038"
                   }
        cart = CartServices()
        result = cart.post_cart_product_gift_front(product=product)
        print(result)
        self.assertEqual(result, result)

    def test_post_cart_product_quantity_front(self):
        product = {"cart_id": "5cc7005eaee7b829e48a4856",
                   "product_id": "5caf535b6eeb6210b46ef4f1",
                   "quantity": 10,
                   "user_id": "5cc6ff57aee7b829e48a4855"
                   }
        cart = CartServices()
        result = cart.post_cart_product_quantity_front(product=product)
        print(result)
        self.assertEqual(result, result)


    def test_get_user_cart_front(self):
        cart = CartServices()
        result = cart.get_user_cart_front(user_id="5c914cf378de470068b0d1d2")
        print(result)
        self.assertEqual(result, result)

    def test_post_user_cart_front(self):

        product = {"user_id": "5c914cf378de470068b0d1d2",
                   "store_id": "5c8c003feaa994293038e8b9",
                   "store_name": "Plie",
                   "product_id": "5c8c003feaa994293038e8b8", # "5c81519fc0f514426c888538",
                   "product_name": "product other",
                   "product_photo": "1",
                   "price": 2,
                   "quantity": 3,
                   "observations": "Test Test Test ok",
                   "gift_from": "",
                   "gift_to": "",
                   "message": "",
                   "gift_flag": ""
                   }

        cart = CartServices()
        result = cart.post_user_cart_front(product=product)
        self.assertEqual(result, result)

    def test_delete_user_cart_store_front(self):
        cart = CartServices()
        result = cart.delete_user_cart_store_front(user_id="5c914cf378de470068b0d1d2",
                                                   store_id="5c8c003feaa994293038e8b9")
        self.assertEqual(result, result)

    def test_delete_user_cart_product_front(self):
        cart = CartServices()
        result = cart.delete_user_cart_product_front(user_id="5c914cf378de470068b0d1d2",
                                                     store_id="5c8c003feaa994293038e8b9",
                                                     product_id="5c8c003feaa994293038e8b8",
                                                     quantity=2)
        self.assertEqual(result, result)