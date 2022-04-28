from unittest import TestCase
from database.database_service.database_review_service import DatabaseReviewsService
import datetime
from constants import C_SUCCESS
from bson import ObjectId


class TestDatabaseBannersService(TestCase):
    def test_get_database_reviews_front(self):
        service = DatabaseReviewsService()
        result = service.get_database_reviews_front(ref_id="5c991bd0eae4fc0f1cb5f2c0")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)


    def test_get_database_reviews(self):
        service = DatabaseReviewsService()
        result = service.get_database_reviews(search_word="te", start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_review(self):
        service = DatabaseReviewsService()
        result = service.get_database_review(review_id="5ce6ce8f9d44a9306ca55092")
        self.assertEqual(result, result)


    def test_insert_review(self):
        service = DatabaseReviewsService()
        review = {"store_code": "test",
                  "store_name": "test",
                  "rating": 4,
                  "date": str(datetime.datetime.now()),
                  "review": "test",
                  "name": "test",
                  "type": "Produto",
                  "status": "Não Lido",
                  "code": "123Plie"}
        result = service.insert_database_review(review=review,
                                                user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_reviews_count(self):
        service = DatabaseReviewsService()
        result = service.get_database_reviews_count(search_word="test")
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_review(self):
        service = DatabaseReviewsService()
        result = service.delete_database_review(review_id="")
        print(result)
        self.assertEqual(result, C_SUCCESS)
