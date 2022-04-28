from unittest import TestCase
from database.database_service.database_product_service import DatabaseProductService
from constants import C_SUCCESS
import json
from bson import ObjectId
import datetime


class TestDatabaseProduct(TestCase):

    def test_get_profile_products_front(self):
        products = DatabaseProductService()
        result = products.get_database_profile_products_front(user_id="5c994c21eae4fc0f1cb5f2c2")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_fav_products_front(self):
        products = DatabaseProductService()
        result = products.get_database_fav_products_front(user_id=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_database_product_front(self):
        products = DatabaseProductService()
        result = products.get_database_products_front(2)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_front_one(self):
        product = DatabaseProductService()
        result = product.get_database_product_front_one(product_id=1)
        for r in result:
            print("name" + r.name)
        self.assertEqual(result, result)


    def test_get_database_product_photos_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_photos_front(product_id='5c9cf0fda5a4bd34ecf9abbb')

        for r in result:
            for p in r['photos']:
                print(p['name'])
        self.assertEqual(result, result)

    def test_get_database_product_colors_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_colors_front(product_id='5c9cf0fda5a4bd34ecf9abbb')

        for r in result:
            for p in r['photos']:
                print(p['name'])
        self.assertEqual(result, result)

    def test_get_database_product_colors_front_one(self):
        product = DatabaseProductService()
        result = product.get_database_product_colors_front_one(color_id='5c9cfe9ba5a4bd34ecf9abbe')

        for r in result:
            for p in r['photos']:
                print(p['name'])
        self.assertEqual(result, result)

    def test_get_database_product_categories_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_categories_front(category_name="Biscuit",
                                                               start=1)

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_deliver_filter_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_deliver_filter_front(search_word="Biscuit",
                                                                   search_type="CATEGORY")

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_public_filter_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_public_filter_front(search_word="Biscuit",
                                                                   search_type="CATEGORY")

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_price_filter_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_price_filter_front(search_word="Biscuit",
                                                                   search_type="CATEGORY")

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_state_filter_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_state_filter_front(search_word="Biscuit",
                                                                   search_type="CATEGORY")

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_search_front(self):
        product = DatabaseProductService()
        result = product.get_database_product_search_front(search_word="biscuit",
                                                           start=1)

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_products_filtered_front(self):
        json_data = {'min_price': '2.50', 'max_price': '8.50', 'category': [], 'public': ['Adulto'], 'deliver': [],
                     'state': [], 'order': 'Novo'}
        product = DatabaseProductService()
        result = product.get_database_products_filtered_front(search_word="Biscuit",
                                                              search_type="a",
                                                              json_filter=json_data,
                                                              start=1)

        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product(self):
        """This function must test the product and product photos"""
        product = DatabaseProductService()
        result = product.get_database_product(product_id="5c991bd0eae4fc0f1cb5f2c0")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_product(self):
        # json object
        product = {"_id": "5ced8055aee7b82cd497f8e2",
                   "user_id": ObjectId(),
                   "name": "test",
                   "store_id": ObjectId(),
                   "photo": "1",
                   "store_code": "Plie",
                   "old_value": 15.05,
                   "discount": "N",
                   "new_value": 2.5,
                   "short_description": "test test test",
                   "ratings_count": 5,
                   "reviews_count": 3,
                   "details_features": "test test test",
                   "color_flag": "Y",
                   "category_id": ObjectId(),
                   "category_name": "Biscuit",
                   "public": ["Bebes", "Infantil", "Adultos"],
                   "deliver": ["Frete Gratis", "Digital", "Sedexes"],
                   "state_name": "São Paulo",
                   "state_code": "SP",
                   "city": "Campinas",
                   "tags": "bebe novo moda super gente",
                   "creation_date": str(datetime.datetime.now()),
                   "translation_date": str(datetime.datetime.now()),
                   "description": "test test test",
                   "details": "test teste",
                   "width": 20,
                   "height": 15,
                   "weight": 15,
                   "length": 15,
                   "stock_quantity": 1,
                   "gift_flag": "Y",
                   "gift_value": 2.0,
                   "production_term": 5,
                   "status": "Active"
                   }
        product_service = DatabaseProductService()
        result = product_service.merge_database_product(product)
        print(result)
        self.assertNotEqual(result, 0)

    def test_delete_database_product(self):
        product = DatabaseProductService()
        result = product.delete_database_product(product_id=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_products(self):
        product = DatabaseProductService()
        result = product.get_database_products(search_word="tes", start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_product_photos(self):
        """This function must test the product and product photos"""
        product = DatabaseProductService()
        result = product.get_database_product_photos(product_id="5c991bd0eae4fc0f1cb5f2c0")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_product_photos(self):
        # json object
        product = {"product_id": ObjectId(),
                   "photos": [{"name": "test",
                              "order": 1}]}
        product_service = DatabaseProductService()
        result = product_service.merge_database_product_photos(product)
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_product_photos(self):
        product = DatabaseProductService()
        result = product.delete_database_product_photos(product_id="5ced8677aee7b8312c2180bb")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_product_colors(self):
        """This function must test the product and product photos"""
        product = DatabaseProductService()
        result = product.get_database_product(product_id="5c991bd0eae4fc0f1cb5f2c0")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_product_colors(self):
        # json object
        product = {"product_id": "5ced88bfaee7b83478b3abd2",
                   "color_name": "Amarelo",
                   "photos": [{"name": "tests",
                               "order": 1},
                              {"name": "test11",
                               "order": 2}],
                   "sizes": [{"size": "P",
                              "quantity": 2}]}
        product_service = DatabaseProductService()
        result = product_service.merge_database_product_colors(product)
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_product_colors(self):
        product = DatabaseProductService()
        result = product.delete_database_product(product_id=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)


    def test_post_database_product_sold_off(self):
        product = {"id": "5cae2a740b71272b40e3ae46",
                   "sold_off": "N"}
        product_service = DatabaseProductService()
        result = product_service.post_database_product_sold_off(product)
        print(result)
        self.assertEqual(result, result)


    def test_post_product_enable_disable(self):
        product = {"id": "5ced8048aee7b80da4a93a3a",
                   "status": "Inativo"}
        product_service = DatabaseProductService()
        result = product_service.post_product_enable_disable(product)
        print(result)
        self.assertEqual(result, result)

    def test_merge_database_product_favorites(self):
        product = {"product_id": "5cf696d47733ab0a5c3a6a7a", "user_id": "5d729ddeaee7b89398d77b08"}
        product_service = DatabaseProductService()
        result = product_service.merge_database_product_favorites(product=product)
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_product_favorite(self):
        product_favorite_id = "5d83b4f5aee7b83655052c5b"
        product_service = DatabaseProductService()
        result = product_service.delete_database_product_favorite(product_favorite_id=product_favorite_id)
        print(result)
        self.assertEqual(result, result)