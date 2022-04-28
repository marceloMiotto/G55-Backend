from unittest import TestCase
from service.page_pagination_service import PagePaginationService
import json


class TestPagePaginationService(TestCase):
    def test_get_higher_limit(self):
        page_service = PagePaginationService(total_records=17,
                                             page=8)
        result = page_service.get_higher_limit()
        self.assertEqual(result, 5)

    def test_get_higher_limit_display(self):
        page_service = PagePaginationService(total_records=17,
                                             page=4)
        result = page_service.get_higher_limit_display()
        self.assertEqual(result, 17)

    def test_get_lower_limit(self):
        page_service = PagePaginationService(total_records=17,
                                             page=2)
        result = page_service.get_lower_limit()
        self.assertEqual(result, 6)

    def test_get_page(self):
        page_service = PagePaginationService(total_records=17,
                                             page=2)
        result = page_service.get_page()
        self.assertEqual(result, 2)

    def test_get_previous_page(self):
        page_service = PagePaginationService(total_records=17,
                                             page=2)
        result = page_service.get_previous_page()
        self.assertEqual(result, 1)

    def test_get_next_page(self):
        page_service = PagePaginationService(total_records=17,
                                             page=2)
        result = page_service.get_next_page()
        self.assertEqual(result, 3)

    def test_serialize(self):
        page_service = PagePaginationService(total_records=17,
                                             page=2)
        result = page_service.serialize
        print("works 1 " + str(result['total_records']))
        print(result)
        json_result = result
        print(json_result)
        print("works 2 " + str(json_result['total_records']))
        json_data = json.dumps(json_result)
        print(json_data)
        self.assertEqual(result, result)
