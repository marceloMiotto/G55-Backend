from unittest import TestCase
from service.category_service import CategoryServices
from constants import C_SUCCESS


class TestCategoryServices(TestCase):
    def test_merge_category_type(self):
        category = {"name": "Produtos", "type": "Produtos"}
        category_service = CategoryServices()
        result = category_service.merge_category(category=category,
                                                 user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_get_categories(self):
        category = CategoryServices()
        result = category.get_categories(total_records=2,
                                         page=1,
                                         search="test",
                                         user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_get_categories_front(self):
        category = CategoryServices()
        result = category.get_categories_front(store_id="",
                                               store_code="ALL")
        print(result)
        self.assertEqual(result, result)

    def test_delete_category_type(self):
        category = CategoryServices()
        result = category.delete_category(category_id="5ddbde34aee7b807712d532f",
                                          user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_get_category_id(self):
        category = CategoryServices()
        result = category.get_category_id(category_name="Biscuit")
        print(result)
        self.assertEqual(result, result)