from unittest import TestCase
from database.database_service.database_messages_service import DatabaseMessageService
import datetime


class TestDatabaseMessageService(TestCase):

    def test_get_database_messages(self):
        service = DatabaseMessageService()
        result = service.get_database_messages(customer_profile_id="5c9d323da5a4bd34ecf9abc2",
                                               store_id="5c9d323da5a4bd34ecf9abc3" )
        print(result)
        for p in result:
            print(p['message'])
        self.assertEqual(result, result)

    def test_post_database_message(self):
        service = DatabaseMessageService()
        message = {"customer_id": "5c9d323da5a4bd34ecf9abc2",
                   "store_id": "5c9d323da5a4bd34ecf9abc3",
                   "product_id": "5c9d323da5a4bd34ecf9abc3",
                   "message": "update test message"
                   }
        result = service.post_database_message(message=message, user_id="")
        print(result)
        self.assertEqual(result, result)



    def test_merge_database_message_user_session(self):
        service = DatabaseMessageService()
        message_session = {"user_id": "5c994c25eae4fc0f1cb5f2c3", "session_id": "12345"}
        result = service.merge_database_messages_session(message_session=message_session)
        print(result)
        self.assertEqual(result, result)


    def testget_database_message_user_session(self):
        service = DatabaseMessageService()
        contact_id = "5c994c25eae4fc0f1cb5f2c3"
        result = service.get_database_messages_session(contact_id=contact_id)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)
