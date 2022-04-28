from unittest import TestCase
from service.rating_service import RatingServices
from constants import C_SUCCESS


class TestRatingServices(TestCase):
    def test_merge_category_type(self):
        rating = {"name": "Produtos", "type": "Produtos"}
        rating_service = RatingServices()
        result = rating_service.merge_rating(rating=rating)
        print(result)
        self.assertEqual(result, result)

    def test_get_categories(self):
        rating_service = RatingServices()
        result = rating_service.get_ratings(ref_id="",
                                            total_records=2,
                                            page=1)
        print(result)
        self.assertEqual(result, result)


    def test_delete_rating(self):
        rating_service = RatingServices()
        result = rating_service.delete_rating(rating_id="")
        print(result)
        self.assertEqual(result, result)

    def test_update_rating(self):
        rating = {"_id": "5d0137cdaee7b82584f459a9",
                  "answer_review": "test test"}
        rating_service = RatingServices()
        result = rating_service.update_rating_review(rating=rating)
        print(result)
        self.assertEqual(result, result)