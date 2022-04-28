from unittest import TestCase
from service.session_service import SessionServices


class TestSessionServices(TestCase):
    def test_get_banners_front(self):
        service = SessionServices()
        result = service.get_session()
        print(result)
        self.assertEqual(result, result)
