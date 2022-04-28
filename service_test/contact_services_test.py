from unittest import TestCase
from service.contact_service import ContactServices
import datetime


class TestContactServices(TestCase):
    def test_insert_contact(self):
        contact_obj = {"name": "test2",
                       "email": "test@gmail.com",
                       "status": "N",
                       "question": "o que?",
                       "creation_date": datetime.datetime.now()}

        contact_service = ContactServices()
        result = contact_service.insert_contact(contact=contact_obj)
        self.assertEqual(result, result)

    def test_upsert_contact(self):
        contact_obj = {"_id": "5ce58535aee7b83354df670e",
                       "answer": "ota patilera 2",
                       "answer_date": datetime.datetime.now()}
        contact_service = ContactServices()
        result = contact_service.upsert_contact(contact=contact_obj)
        self.assertEqual(result, result)

    def test_get_contacts_count(self):
        contact_service = ContactServices()
        result = contact_service.get_contacts_count(search="test")
        print(result)
        self.assertEqual(result, result)

    def test_get_contacts(self):
        contact_service = ContactServices()
        result = contact_service.get_contacts(total_records=4,
                                              page=1,
                                              search="test")
        print(result)
        for r in result['rows']:
            print(r)
        self.assertEqual(result, result)

    def test_delete_contact(self):
        contact_service = ContactServices()
        result = contact_service.delete_contact(contact_id=1)
        self.assertEqual(result, result)
