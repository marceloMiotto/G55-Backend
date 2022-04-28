from unittest import TestCase
from service.favorites_service import FavoritesServices


class TestProductServices(TestCase):

    def test_merge_fav_products_front(self):
        favorite = {"product_id": "5cf696d67733ab0a5c3a6a7b", "user_id": "5d729ddeaee7b89398d77b08", "type":"PRODUCT"}
        favorite_service = FavoritesServices()
        result = favorite_service.merge_favorites(favorite=favorite,
                                                  user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_fav_products_front(self):
        favorite_id = "5d83b5b5aee7b89d305d5eb2"
        favorite_service = FavoritesServices()
        result = favorite_service.delete_favorite(favorite_id=favorite_id,
                                                  user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_products_favorites(self):
        user_id = "5d729ddeaee7b89398d77b08"
        favorite_service = FavoritesServices()
        result = favorite_service.get_products_favorites(user_id=user_id)
        print(result)
        self.assertEqual(result, result)

    def test_get_stores_favorites(self):
        user_id = "5d729ddeaee7b89398d77b08"
        favorite_service = FavoritesServices()
        result = favorite_service.get_stores_favorites(user_id=user_id)
        print(result)
        self.assertEqual(result, result)