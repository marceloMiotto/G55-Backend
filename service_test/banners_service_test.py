from unittest import TestCase
from service.banners_service import BannersServices


class TestBannersServices(TestCase):
    def test_get_banners_front(self):
        service = BannersServices()
        result = service.get_banners_front(store_id="5d7bfc56f3150c2eb1a96d19")
        print(result)
        self.assertEqual(result, result)
