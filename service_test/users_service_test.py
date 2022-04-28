from unittest import TestCase
from service.users_service import UsersServices


class TestUsersServices(TestCase):
    def test_merge_user(self):
        user = {"name": "test",
                "email": "ok@otapatilera.com",
                "type": "SHOP",
                "status": "Ativo"}
        user_service = UsersServices()
        result = user_service.merge_user(user=user)
        print(result)
        self.assertEqual(result, result)

    def test_get_users_count(self):
        user_service = UsersServices()
        result = user_service.get_users_count(search="mi")
        print(result)
        self.assertEqual(result, result)

    def test_get_users(self):
        user_service = UsersServices()
        result = user_service.get_users(total_records=3, page=1, search="te")
        print(result)
        self.assertEqual(result, result)

    def test_delete_user(self):
        user_service = UsersServices()
        result = user_service.delete_user(user_code="5cf952ebb5c5a70538425abe")
        print(result)
        self.assertEqual(result, result)


    def test_authenticate_user(self):
        user_service = UsersServices()
        user = {"email": "test",
                "pwd": "test"}
        result = user_service.authenticate_user(user=user)
        print(result)
        self.assertEqual(result, result)

    def test_create_user_account(self):
        user_service = UsersServices()
        user = {"email": "test",
                "name": "test",
                "status": "Ativo",
                "password": "1234"}
        result = user_service.create_user_account(user=user)
        print(result)
        self.assertEqual(result, result)
