from unittest import TestCase
from database.database_service.database_standard_message_service import DatabaseStandardMessageService
from constants import C_EXISTS, C_SUCCESS
from bson import ObjectId
import datetime


class TestDatabaseStandardMessageService(TestCase):

    def test_get_standard_messages(self):
        messages = DatabaseStandardMessageService()
        result = messages.get_database_standard_messages(user_id="",
                                                         search_word="te",
                                                         start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_delete_standard_messages(self):
        message = DatabaseStandardMessageService()
        result = message.delete_database_standard_messages(message_id="5dd8193caee7b8d7406aa716",
                                                           user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

    def test_merge_standard_message(self):
        message = DatabaseStandardMessageService()
        smessage = {"message_key": "AB",
                    "message_text": "test"
                    }
        result = message.merge_database_standard_message(smessage=smessage,
                                                         user_id="5d729ddeaee7b89398d77b08")
        print(result)

        self.assertEqual(result, result)

    def test_get_count(self):
        message = DatabaseStandardMessageService()
        result = message.get_database_standard_message_count(user_id="5d729ddeaee7b89398d77b08",
                                                             search="tes")
        print(result)
        self.assertNotEqual(result, 0)
