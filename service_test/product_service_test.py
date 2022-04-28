from unittest import TestCase
from service.product_service import ProductServices
from constants import C_SUCCESS
from bson import ObjectId
import datetime


class TestProductServices(TestCase):

    def test_get_profile_products_front(self):
        products = ProductServices()
        result = products.get_profile_products_front(profile_id="5c994c21eae4fc0f1cb5f2c2")
        self.assertEqual(result, result)

    def test_get_products_covers_front(self):
        products = ProductServices()
        result = products.get_products_covers_front(start=0)
        for r in result:
            print(r.name)
        self.assertEqual(result, result)

    def test_get_product_front_one(self):
        product = ProductServices()
        result = product.get_product_front_one(product_id=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_product_photos_front(self):
        product = ProductServices()
        result = product.get_product_photos_front(product_id='5c9cf0fda5a4bd34ecf9abbb')
        print(result)
        self.assertEqual(result, result)

    def test_get_product_colors_front(self):
        product = ProductServices()
        result = product.get_product_colors_front(product_id='5c991bd0eae4fc0f1cb5f2c0')
        print(result)
        self.assertEqual(result, result)

    def test_get_product_colors_front_one(self):
        product = ProductServices()
        result = product.get_product_colors_front_one(color_id='5c9cfe9ba5a4bd34ecf9abbe')
        print(result)
        self.assertEqual(result, result)

    def test_get_product_categories_front(self):
        product = ProductServices()
        result = product.get_product_categories_front(category_name="Biscuit",
                                                      start=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_product_search_front(self):
        product = ProductServices()
        result = product.get_product_search_front(search_word="Biscuit",
                                                  start=1)
        print(result)
        self.assertEqual(result, result)

    def test_get_product_public_filter_front(self):
        product = ProductServices()
        result = product.get_product_public_filter_front(search_word="Biscuit",
                                                         search_type="CATEGORY")
        print(result)
        self.assertEqual(result, result)

    def test_get_product_deliver_filter_front(self):
        product = ProductServices()
        result = product.get_product_deliver_filter_front(search_word="Biscuit",
                                                          search_type="CATEGORY")
        print(result)
        self.assertEqual(result, result)

    def test_get_product_price_filter_front(self):
        product = ProductServices()
        result = product.get_product_price_filter_front(search_word="Biscuit",
                                                        search_type="CATEGORY")
        print(result)
        self.assertEqual(result, result)

    def test_get_product_state_filter_front(self):
        product = ProductServices()
        result = product.get_product_state_filter_front(search_word="Biscuit",
                                                        search_type="CATEGORY")
        print(result)
        self.assertEqual(result, result)

    def test_get_product_category_filter_front(self):
        product = ProductServices()
        result = product.get_product_category_filter_front(search_word="Biscuit",
                                                           search_type="CATEGORY")
        print(result)
        self.assertEqual(result, result)

    def test_get_products_search_filtered_front(self):
        json_data = {'min_price': '2.50', 'max_price': '7.50', 'category': [], 'public': ['Adulto'], 'deliver': [],
                     'state': [], 'order': '--- Ordenar por ---'}
        product = ProductServices()
        result = product.get_products_filtered_front(search_word="Test",
                                                     search_type="a",
                                                     json_filter=json_data,
                                                     start=1)
        print(result)
        self.assertEqual(result, result)


    def test_post_product(self):
        product = {"_id": "5ced8055aee7b82cd497f8e2",
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

        product_service = ProductServices()
        result = product_service.post_product(product=product,
                                              user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_product(self):
        product = ProductServices()
        result = product.get_product(product_id="5c991bd0eae4fc0f1cb5f2c0",
                                     user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_product(self):
        product = ProductServices()
        result = product.delete_product(product_id="5c991bd0eae4fc0f1cb5f2c0",
                                        user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_post_product_sold_off(self):
        product = {"id": "5cae2a740b71272b40e3ae46",
                   "sold_off": "Y"}
        product_service = ProductServices()
        result = product_service.post_product_sold_off(product=product,
                                                       user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_post_product_enable_disable(self):
        product = {"id": "5ced8048aee7b80da4a93a3a",
                   "status": "Ativo"}
        product_service = ProductServices()
        result = product_service.post_product_enable_disable(product=product,
                                                             user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_save_product_photo(self):
        product = ProductServices()
        image = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFRUXGR8aGBcYGCAeIBseGxoaHhsgIhsiHykgGx0lHRobITEjJSkrLi4wGh8zODMwOCgtLisBCgoKDg0OGxAQGzMmICUtMi0xMjIyLS0vLS01Ly01LjAwLS8tMi0vNy0tLS8tLS0rLS0tLS0vLS0tLS0tLy0vLf/AABEIALcBEwMBEQACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAAABQMEBgIBBwj/xAA8EAACAQMCBQIEBAUCBQUBAAABAhEAAyESMQQFIkFRYXEGEzKBQlKRoQcUI7HRweEVM4Lw8UNicpKiFv/EABoBAQADAQEBAAAAAAAAAAAAAAACAwQBBQb/xAA1EQABAwMCAwYFBQEBAAMBAAABAAIRAyExEkEEUWETInGBkfAyobHB0QUUQuHxUiMVM4IG/9oADAMBAAIRAxEAPwD4bREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFERREURFEXoFEWk5T8EcXeOU+WsTLf4Ga7CiXtGTC0j/wANLa6dXEsTpkwkCfSa7CrPEUv+lVP8Ox2vMSJJ6O3aKaU7dm5SzjPgS+n0urYmDK47VzSV0VmEmDhZzjeAuWjFxCp9a4rAQVWouptyn4a4riINqy5U/jIhf/scH7V0BRc7TsT4D381o7X8OXH/ADuJs243AOo/4rhgLgFU4bA6n7CVds/AvBhZa/euQc6FA+2xzXRfAXXVKdM6ajwD6fVNj8JcAAtwcLcZJ2a9v4wCD6QK6GnkqP3/AAuot1Kbi/gvgbfW3CXNB7i6/T/gD1mpdmVW39S4d2J/P9qsfgLgiMJehz0OLkgSMD6d/euadlKnx/DvEzHj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"
        store_id = "5d684067aee7b83d28ae52b3"
        file_name = "1"

        result = product.save_product_photos(image=image, store_id=store_id, file_name=file_name)
        self.assertEqual(result, result)


    def test_merge_fav_products_front(self):
        product = {"product_id": "5cf696d67733ab0a5c3a6a7b", "user_id": "5d729ddeaee7b89398d77b08"}
        product_service = ProductServices()
        result = product_service.merge_fav_products_front(product=product)
        print(result)
        self.assertEqual(result, result)

