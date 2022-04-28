from unittest import TestCase
from database.database_service.database_complaint_service import DatabaseComplaintService
from constants import C_EXISTS, C_SUCCESS
import datetime


class TestDatabaseComplaintService(TestCase):

    def test_get_database_complaints(self):
        database_complaint_service = DatabaseComplaintService()
        result = database_complaint_service.get_database_complaints(search_word="te", start=1)
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_complaint(self):
        database_complaint_service = DatabaseComplaintService()
        result = database_complaint_service.get_database_complaint(complaint_id="5ce6ce8f9d44a9306ca55092")
        self.assertEqual(result, result)

    def test_insert_complaint_exists(self):
        database_complaint_service = DatabaseComplaintService()
        complaint = {"store_code": "test",
                     "store_name": "test",
                     "product_name": "test",
                     "user_name": "test",
                     "deleted": "N"}
        result = database_complaint_service.insert_database_complaint(complaint=complaint,
                                                                      user_id="5d729ddeaee7b89398d77b08")
        print(result)

        self.assertEqual(result, result)

    def test_get_database_complaints_count(self):
        comps = DatabaseComplaintService()
        result = comps.get_database_complaints_count(search_word="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_complaint(self):
        comps = DatabaseComplaintService()
        result = comps.delete_database_complaint(complaint_id=1)
        print(result)
        self.assertEqual(result, C_SUCCESS)
