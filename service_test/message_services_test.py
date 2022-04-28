from unittest import TestCase
from service.messages_service import MessageServices
import datetime


class TestMessageServices(TestCase):

    def test_get_messages_front(self):
        service = MessageServices()
        result = service.get_messages(customer_id="5c9d323da5a4bd34ecf9abc2",
                                      store_id="5c9d323da5a4bd34ecf9abc3")
        print(result)
        self.assertEqual(result, result)

    def test_post_message_front(self):
        service = MessageServices()
        message = {"customer_id": "5c9d323da5a4bd34ecf9abc2",
                   "store_id": "5c9d323da5a4bd34ecf9abc3",
                   "product_id": "5c9d323da5a4bd34ecf9abc3",
                   "message": "update test message"
                   }
        result = service.post_message(message=message)
        print(result)
        self.assertEqual(result, result)


    def test_get_messages_user_session(self):
        service = MessageServices()
        contact_id = "5c994c25eae4fc0f1cb5f2c3"
        result = service.get_messages_session(contact_id=contact_id)
        print(result)
        self.assertEqual(result, result)

    def test_merge_register_message_user_session(self):
        service = MessageServices()
        message_session = {"user_id": "5c994c25eae4fc0f1cb5f2c3", "session_id": "12345"}
        result = service.merge_messages_session(message_session=message_session)
        print(result)
        self.assertEqual(result, result)



