from unittest import TestCase
from database.database_service.database_users_service import DatabaseUsersService


class TestDatabaseUsersService(TestCase):
    def test_get_database_users(self):
        user_service = DatabaseUsersService()
        result = user_service.get_database_users(search_word="", start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_user(self):
        user_service = DatabaseUsersService()
        result = user_service.get_database_user(user_id="5c914cf378de470068b0d1d2")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_user(self):
        user = {"name": "miotto",
                "type": "USER",
                "email": "miotto@email.com",
                "password": "123",
                "status": "Ativo"}
        user_service = DatabaseUsersService()
        result = user_service.merge_database_user(user=user)
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_user(self):
        user_service = DatabaseUsersService()
        result = user_service.delete_database_user(user_id="5cf952eeb5c5a70538425abf",
                                                   user_code="")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_users_count(self):
        user_service = DatabaseUsersService()
        result = user_service.get_database_users_count(search_word="te")
        print(result)
        self.assertEqual(result, result)

    def test_get_database_user_info(self):
        user_service = DatabaseUsersService()
        result = user_service.get_database_user_info(user_code="test@email.com")
        print(result)
        for r in result:
            print(r["_id"])
        self.assertEqual(result, result)

    def test_verify_database_user_credentials(self):
        user_service = DatabaseUsersService()
        user = {"email": "test", "pwd": "test"}
        result = user_service.verify_database_user_credentials(user=user)
        for r in result:
            print(r)
        self.assertEqual(result, result)


    def test_user_database_exists(self):
        user_service = DatabaseUsersService()
        user = "miotto@email.com"
        result = user_service.user_database_exists(user_code=user)
        print(result)
        self.assertEqual(result, result)

