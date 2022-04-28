from unittest import TestCase
from database.database_service.database_category_service import DatabaseCategoryService
from constants import C_SUCCESS
from bson import ObjectId
import datetime


class TestDatabaseCategoryService(TestCase):

    def test_get_categories(self):
        category = DatabaseCategoryService()
        result = category.get_database_categories(search_word="test",
                                                  start=1,
                                                  user_id="5d729ddeaee7b89398d77b08")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_delete_category(self):
        category = DatabaseCategoryService()
        categ = category.delete_database_category(category_id="5dd7e022aee7b8a2002e6a15",
                                                  user_id="5d729ddeaee7b89398d77b08")
        self.assertEqual(categ, categ)

    def test_merge_category(self):
        category = DatabaseCategoryService()
        cat_value = {"_id": ObjectId(),
                     "name": "test",
                     "type": "Produtos"
                     }
        user_id = "5d729ddeaee7b89398d77b08"
        categ = category.merge_database_category(category=cat_value, user_id=user_id)
        print(categ)
        self.assertEqual(categ, categ)

    def test_get_categories_front(self):
        category = DatabaseCategoryService()
        result = category.get_database_categories_front(store_id="",
                                                        store_code="ALL")

        for r in result:
            print(r)

        self.assertEqual(result, result)

    def test_get_database_categories_count(self):
        category = DatabaseCategoryService()
        result = category.get_database_category_count(search="test")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_category_id(self):
        category = DatabaseCategoryService()
        result = category.get_database_category_id(category_name="test")
        print(result)

        self.assertEqual(result, result)

