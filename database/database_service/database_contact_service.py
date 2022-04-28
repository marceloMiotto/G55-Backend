from constants import C_ADMIN_PAGE_SIZE, C_UPDATING_ERROR, C_INSERTING_ERROR, \
    C_GETTING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE
from service.log_service import log_database
from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
import datetime
from constants import C_DATE_MASK
from service.utils_service import success_to_json, error_to_json


class DatabaseContactService(object):
    def __init__(self):
        pass

    def get_database_contacts_count(self, search_word):
        try:
            mc = MongoCollection()
            col = mc.contacts()
            return col.count_documents({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                       {"email": {"$regex": search_word, "$options": 'i'}},
                                       {"subject": {"$regex": search_word, "$options": 'i'}},
                                       ]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_contacts_count", "Getting", str(e), search_word))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_contacts(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.contacts()
            return col.find({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                     {"email": {"$regex": search_word, "$options": 'i'}},
                                     {"subject": {"$regex": search_word, "$options": 'i'}},
                                     ]}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_contacts", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_contact(self, contact_id):
        try:
            mc = MongoCollection()
            col = mc.contacts()
            col.delete_one({"_id": ObjectId(contact_id)})

            return success_to_json(contact_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_contact", "Deleting", str(e), contact_id))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def insert_database_contact(self, contact):
        try:
            print("debug contact")
            mc = MongoCollection()
            col = mc.contacts()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            contact["creation_date"] = dt
            r = col.insert_one(contact).inserted_id

            return success_to_json(str(r))

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("insert_database_contact", "Inserting", str(e), contact))
            print(str(e))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))

    def upsert_database_contact_answer(self, contact):
        try:

            print("debug contact")
            mc = MongoCollection()
            col = mc.contacts()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            col.update_one({'_id': ObjectId(contact['_id'])},
                           {'$set': {'answer': contact['answer'],
                                     'answer_date': dt,
                                     'status': "Y"}}
                           )

            return success_to_json(contact['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("upsert_database_contact_answer", "Updating", str(e), contact))
            print(str(e))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))



