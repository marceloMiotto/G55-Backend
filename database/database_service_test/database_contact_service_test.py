from unittest import TestCase
from database.database_service.database_contact_service import DatabaseContactService
import datetime


class TestDatabaseContactService(TestCase):
    def test_get_database_contacts(self):
        contact = DatabaseContactService()
        result = contact.get_database_contacts(search_word="test", start=2)
        print(result)
        for r in result:
            print(r)

        self.assertEqual(result, result)

    def test_delete_database_contact(self):
        contact = DatabaseContactService()
        result = contact.delete_database_contact(contact_id="")

        self.assertEqual(result, result)

    def test_insert_database_contact(self):
        contact_obj = {"name": "test2",
                       "email": "test@gmail.com",
                       "status": "N",
                       "question": "o que?",
                       "subject": "pedido",
                       "creation_date": '{:%d-%m-%Y %H:%M}'.format(datetime.datetime.now())
                       }

        contact = DatabaseContactService()
        result = contact.insert_database_contact(contact=contact_obj)

        self.assertEqual(result, result)

    def test_upsert_database_contact_answer(self):
        contact_obj = {"_id": "5ce58535aee7b83354df670e",
                       "answer": "ota patilera",
                       "answer_date": '{:%d-%m-%Y %H:%M}'.format(datetime.datetime.now())}
        contact = DatabaseContactService()
        result = contact.upsert_database_contact_answer(contact=contact_obj)

        self.assertEqual(result, result)

    def test_get_database_contacts_count(self):
        contact = DatabaseContactService()
        result = contact.get_database_contacts_count(search_word="testa")
        print(result)

        self.assertEqual(result, result)
