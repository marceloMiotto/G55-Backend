from unittest import TestCase
from service.review_service import ReviewServices
import datetime
from bson import ObjectId


class TestBannersServices(TestCase):
    def test_get_reviews_front(self):
        service = ReviewServices()
        result = service.get_reviews_front(ref_id='')
        print(result)
        self.assertEqual(result, result)

    def test_insert_review(self):
        review = {"store_name": "test",
                  "store_code": "test",
                  "rating": 4,
                  "date": str(datetime.datetime.now()),
                  "review": "test",
                  "name": "test",
                  "type": "Produto",
                  "status": "Não Lido",
                  "creation_date": str(datetime.datetime.now()),
                  "store_id": ObjectId()
                  }

        contact_service = ReviewServices()
        result = contact_service.insert_review(review=review,
                                               user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_reviews_count(self):
        service = ReviewServices()
        result = service.get_reviews_count(search="test",
                                           user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_reviews(self):
        service = ReviewServices()
        result = service.get_reviews(total_records=4,
                                     page=1,
                                     search="test",
                                     user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_review(self):
        service = ReviewServices()
        result = service.delete_review(review_id="5ce6f315aee7b826486da862",
                                       user_id="")
        print(result)
        self.assertEqual(result, result)
