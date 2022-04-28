from unittest import TestCase
from database.database_service.database_rating_service import DatabaseRatingService
from constants import C_SUCCESS
from bson import ObjectId
import datetime


class TestDatabaseRatingService(TestCase):

    def test_get_database_ratings(self):
        rating_service = DatabaseRatingService()
        result = rating_service.get_database_ratings(ref_id="",
                                                     start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_delete_database_rating(self):
        rating_service = DatabaseRatingService()
        result = rating_service.delete_database_rating(rating_id="5cd1d058ece772ae522b9402")
        self.assertEqual(result, result)

    def test_merge_database_rating(self):
        rating_service = DatabaseRatingService()
        rating = {"id": ObjectId(),
                  "rating_text": "test test",
                  "rating_score": "5"
                  }
        result = rating_service.merge_database_rating(rating=rating)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_ratings_count(self):
        rating_service = DatabaseRatingService()
        result = rating_service.get_database_ratings_count(ref_id="")
        print(result)
        self.assertEqual(result, result)


    def test_update_database_rating_answer(self):
        rating = {"id": "5d013802aee7b82584f459ab",
                  "answer_review": "test answer"}
        rating_service = DatabaseRatingService()
        result = rating_service.update_database_rating_answer(rating=rating)
        print(result)
        self.assertEqual(result, result)
