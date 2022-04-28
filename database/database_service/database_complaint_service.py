from constants import C_EXISTS, C_DATE_MASK, C_ADMIN_PAGE_SIZE, \
    C_UPDATING_ERROR, C_DELETING_ERROR, C_INSERTING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE
from service.log_service import log_database
from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
from service.utils_service import success_to_json, error_to_json
import datetime


class DatabaseComplaintService(object):
    def __init__(self):
        pass

    def get_database_complaints(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.complaints()
            return col.find({"$or": [{"store_name": {"$regex": search_word, "$options": 'i'}},
                                     {"product_name": {"$regex": search_word, "$options": 'i'}},
                                     {"user_name": {"$regex": search_word, "$options": 'i'}},
                                     ],
                             "$and": [{"deleted": "N"}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_complaints", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_complaint(self, complaint_id):
        try:
            mc = MongoCollection()
            col = mc.complaints()
            return col.find({"_id": ObjectId(complaint_id)}, {"user_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_complaint", "Getting", str(e), complaint_id ))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_complaints_count(self, search_word):
        try:
            mc = MongoCollection()
            col = mc.complaints()
            return col.count_documents({"$or": [{"store_name": {"$regex": search_word, "$options": 'i'}},
                                       {"product_name": {"$regex": search_word, "$options": 'i'}},
                                       {"user_name": {"$regex": search_word, "$options": 'i'}},
                                       ],
                                       "$and": [{"deleted": "N"}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_complaints_count", "Getting", str(e), search_word))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def insert_database_complaint(self, complaint, user_id):
        try:
            mc = MongoCollection()
            col = mc.complaints()
            dt = datetime.datetime.now()
            complaint["creation_date"] = dt
            complaint["user_id"] = ObjectId(user_id)

            r = col.insert_one(complaint).inserted_id

            return success_to_json(str(r))

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("insert_database_complaint", "Inserting", str(e), complaint))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))

    def delete_database_complaint(self, complaint_id):
        try:
            mc = MongoCollection()
            col = mc.complaints()
            col.update_one({"_id": ObjectId(complaint_id)},
                           {'$set': {'deleted': "Y"}})

            return success_to_json(complaint_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("insert_database_complaint", "Deleting", str(e), complaint_id))
            return error_to_json(C_DELETING_ERROR.format(str(e)))
