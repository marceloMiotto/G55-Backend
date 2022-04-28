from unittest import TestCase
from database.database_service.database_favorites_service import DatabaseFavoritesService
from bson import ObjectId


class TestDatabaseProduct(TestCase):

    def test_merge_database_favorites(self):
        product = {"favorite_id": "5cf696d47733ab0a5c3a6a7a", "type":"PRODUCT"}
        product_service = DatabaseFavoritesService()
        result = product_service.merge_database_favorites(favorite=product, user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_favorite(self):
        favorite_id = "5cf696d47733ab0a5c3a6a7a"
        product_service = DatabaseFavoritesService()
        result = product_service.delete_database_favorite(favorite_id=favorite_id,
                                                          user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_favorite_products(self):
        user_id = "5d729ddeaee7b89398d77b08"
        favorite_service = DatabaseFavoritesService()
        result = favorite_service.get_database_favorite_products(user_id=user_id)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_favorite_stores(self):
        user_id = "5d729ddeaee7b89398d77b08"
        favorite_service = DatabaseFavoritesService()
        result = favorite_service.get_database_favorite_stores(user_id=user_id)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)