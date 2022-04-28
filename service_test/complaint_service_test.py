from unittest import TestCase
from constants import C_EXISTS, C_SUCCESS
from service.complaints_service import ComplaintServices
import datetime
from bson import ObjectId


class TestComplaintServices(TestCase):

    def test_insert_complaint_success(self):
        complaint = {"store_name": "test",
                     "product_name": "test",
                     "user_name": "test",
                     "creation_date": str(datetime.datetime.now()),
                     "store_id": ObjectId(),
                     "product_id": ObjectId(),
                     "deleted": "N"
                     }
        complaint_service = ComplaintServices()
        result = complaint_service.insert_complaint(complaint=complaint)

        self.assertEqual(result, result)


    def test_get_complaints(self):
        complaint = ComplaintServices()
        result = complaint.get_complaints(total_records=2, page=1, search="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_complaint(self):
        complaint = ComplaintServices()
        result = complaint.delete_complaint(complaint_id="5ce6decf575721306c2a96f9")
        print(result)
        self.assertEqual(result, result)

    def test_get_complaint(self):
        complaint = ComplaintServices()
        result = complaint.get_complaint(complaint_id="5ce6ce8f9d44a9306ca55092")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)
