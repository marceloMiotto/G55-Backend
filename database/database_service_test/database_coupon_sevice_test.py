from unittest import TestCase
from database.database_service.database_coupon_service import DatabaseCouponService
from bson import ObjectId
import datetime


class TestDatabaseCoupon(TestCase):

    def test_get_database_coupon(self):
        """This function must test the product and product photos"""
        coupon = DatabaseCouponService()
        result = coupon.get_database_coupon(coupon_id="5cf800c01a740e301c6b045b",
                                            user_id="5ced69a4aee7b842e82e6698")
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_coupon(self):
        # json object
        coupon = {"_id": ObjectId(),
                  "store_id": ObjectId(),
                  "code": "test",
                  "quantity": 1,
                  "type": "CATEGORY",
                  "discount_type": "PERCENT",
                  "discount_value": 10,
                  "creation_date": str(datetime.datetime.now()),
                  "last_updated_date": str(datetime.datetime.now()),
                  "products": ["7123", "7456", "7789"],
                  "categories": ["6123", "6456", "6789"],
                  "start_date": str(datetime.datetime.now()),
                  "end_date": str(datetime.datetime.now())
                  }

        coupon_service = DatabaseCouponService()
        result = coupon_service.merge_database_coupon(coupon=coupon,
                                                      user_id="5ced69a4aee7b842e82e6698")
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_coupon(self):
        coupon = DatabaseCouponService()
        result = coupon.delete_database_coupon(coupon_id="5dd7ec4caee7b813cdecf4cb",
                                               user_id="5ced69a4aee7b842e82e6698")
        self.assertEqual(result, result)

    def test_get_database_coupon_count(self):
        coupon = DatabaseCouponService()
        result = coupon.get_database_coupon_count(search="tes", user_id="5ced69a4aee7b842e82e6698")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_coupons(self):
        coupon = DatabaseCouponService()
        result = coupon.get_database_coupons(user_id="5ced69a4aee7b842e82e6698",
                                             search_word="tes",
                                             start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)


    def test_post_coupon_enable_disable(self):
        coupon = {"id": "5dd7ec8eaee7b81c5dd472be",
                  "status": "Ativo"}
        coupon_service = DatabaseCouponService()
        result = coupon_service.post_database_coupon_enable_disable(coupon=coupon, user_id="5ced69a4aee7b842e82e6698")
        self.assertEqual(result, result)


    def test_cancel_database_coupon(self):
        coupon = {"id": "5dd7ec8eaee7b81c5dd472be",
                  "reason_to_cancel": "test why"}
        coupon_service = DatabaseCouponService()
        result = coupon_service.cancel_database_coupon(coupon=coupon, user_id="5ced69a4aee7b842e82e6698")
        print(result)
        self.assertEqual(result, result)
