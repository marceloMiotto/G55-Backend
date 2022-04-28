from constants import C_EXISTS, C_DATE_MASK, C_ADMIN_PAGE_SIZE, C_GETTING_ERROR, \
    C_DELETING_ERROR, C_UPDATING_ERROR, C_INSERTING_ERROR, C_LOG_MESSAGE
from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from bson import ObjectId
import logging
import datetime
from service.utils_service import success_to_json, error_to_json


class DatabaseStandardMessageService(object):
    def __init__(self):
        pass

    def get_database_standard_messages(self, user_id, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.standard_messages()
            return col.find({"$or": [{"message_key": {"$regex": search_word, "$options": 'i'}},
                                     {"message_text": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_standard_messages", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_standard_message_count(self, user_id, search):
        arguments = ""
        try:
            arguments = "search: " + search
            mc = MongoCollection()
            col = mc.standard_messages()
            return col.count_documents({"$or": [{"message_key": {"$regex": search, "$options": 'i'}},
                                       {"message_text": {"$regex": search, "$options": 'i'}}
                                       ],
                                        "$and": [{"user_id": ObjectId(user_id)}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_standard_message_count", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_standard_messages(self, user_id, message_id):
        arguments = ""
        try:
            arguments = "message_id: " + message_id
            mc = MongoCollection()
            col = mc.standard_messages()
            col.delete_one({"_id": ObjectId(message_id), "user_id": ObjectId(user_id)})

            return success_to_json(message_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_standard_messages", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def merge_database_standard_message(self, smessage, user_id):
        arguments = ""
        try:
            arguments = smessage
            mc = MongoCollection()
            col = mc.standard_messages()
            dt = datetime.datetime.now()
            smessage_id = smessage.get("id", None)
            result = col.update_one({"_id": ObjectId(smessage_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'message_key': smessage['message_key'],
                                              'message_text': smessage['message_text'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    smessage["user_id"] = ObjectId(user_id)
                    smessage["creation_date"] = dt
                    r = col.insert_one(smessage).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_standard_message", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(smessage['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_standard_message", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

