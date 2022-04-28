from unittest import TestCase
from service.token_service import CodeServices


class TestCodeServices(TestCase):
    def test_token_encode(self):
        code = CodeServices()
        user = {"_id": "1234"}
        result = code.token_encode(user)
        print(result)
        self.assertEqual(result, result)
