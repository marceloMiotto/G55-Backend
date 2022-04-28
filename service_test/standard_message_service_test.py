from unittest import TestCase
from service.standard_message_service import StandardMessageService
from constants import C_SUCCESS


class TestStandardMessageServices(TestCase):
    def test_merge_standard_message(self):
        smessage = {"_id": "5cf01a54aee7b82b88609626", "message_key": "test", "message_text": "test"}
        message = StandardMessageService()
        result = message.merge_standard_message(smessage=smessage,
                                                user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_standard_messages(self):
        message = StandardMessageService()
        result = message.get_standard_messages(total_records=12, page=1, search="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_standard_message(self):
        message = StandardMessageService()
        result = message.delete_standard_message(message_id="5cec413baee7b80588cc712a",
                                                 user_id="")
        print(result)
        self.assertEqual(result, result)
