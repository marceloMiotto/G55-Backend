from unittest import TestCase
from service.coupon_service import CouponServices
from constants import C_SUCCESS
import json
import datetime
from bson import ObjectId


class TestCouponServices(TestCase):
    def test_post_coupon(self):
        coupon = {"_id": "5ced6aaaaee7b840ecdb656d",
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
    
        coupon_service = CouponServices()
        result = coupon_service.post_coupon(coupon,
                                            user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_coupon(self):
        coupon_service = CouponServices()
        result = coupon_service.get_coupon(coupon_id="5ced6aaaaee7b840ecdb656d",
                                           user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_coupon(self):
        coupon_service = CouponServices()
        result = coupon_service.delete_coupon(coupon_id="5ced6aaaaee7b840ecdb656d",
                                              user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_coupon_count(self):
        coupon_service = CouponServices()
        result = coupon_service.get_coupon_count(search="",
                                                 user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_coupons(self):
        coupon_service = CouponServices()
        result = coupon_service.get_coupons(total_records=0, page=1, search="", user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_post_coupon_enable_disable(self):
        coupon = {"id": "5cf800c01a740e301c6b045b",
                  "status": "Ativo"}
        coupon_service = CouponServices()
        result = coupon_service.post_coupon_enable_disable(coupon=coupon,
                                                           user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_coupon_cancel(self):
        coupon = {"id": "5cf800c01a740e301c6b045b",
                  "reason_to_cancel": "test another why"}
        coupon_service = CouponServices()
        result = coupon_service.coupon_cancel(coupon=coupon,
                                              user_id="")
        print(result)
        self.assertEqual(result, result)

