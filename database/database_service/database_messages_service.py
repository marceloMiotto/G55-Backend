from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
from service.log_service import log_database
from constants import C_INSERTING_ERROR, C_UPDATING_ERROR, C_DELETING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE, C_DATE_MASK
from service.utils_service import success_to_json, error_to_json
import datetime


class DatabaseMessageService(object):
    def __init__(self):
        pass

    def get_database_messages(self, customer_profile_id, store_id):
        arguments = ""
        try:
            arguments = "customer_id: " + customer_profile_id + "store_id: " + store_id
            mc = MongoCollection()
            col = mc.messages()
            return col.find({'$and': [{'customer_id': ObjectId(customer_profile_id)}, {'store_id': ObjectId(store_id)}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_messages", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def post_database_message(self, message, user_id):
        """Add messages to a conversation"""
        try:
            mc = MongoCollection()
            col = mc.messages()
            message_id = col.insert_one({"customer_profile_id": ObjectId(message['customer_profile_id']),
                                         "store_id": ObjectId(message['store_id']),
                                         "product_id": ObjectId(message['product_id']),
                                         "message_date": datetime.datetime.now(),
                                         "message": message['message'],
                                         "status": "NEW",
                                         "user_id": ObjectId(user_id)
                                         }).inserted_id

            return success_to_json(str(message_id))

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_message_front", "Inserting", str(e), message))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))

    def merge_database_messages_session(self, message_session):
        try:
            mc = MongoCollection()
            col = mc.messages_session()
            contact_id = message_session.get("contact_id", None)
            result = col.update_one({"contact_id": ObjectId(contact_id)},
                                    {"$set": {"session_id": message_session["session_id"],
                                              "updated_date": datetime.datetime.now()}})

            if result.matched_count <= 0:
                try:
                    message_session["creation_date"] = datetime.datetime.now()  #TODO review all creation_date fields from all files, change the type
                    message_session["contact_id"] = ObjectId(message_session["contact_id"])
                    r = col.insert_one(message_session).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_messages_session", "Inserting", str(e), message_session))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(message_session['contact_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_message_session", "Updating", str(e), message_session))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_messages_session(self, contact_id):
        try:
            mc = MongoCollection()
            col = mc.messages_session()
            return col.find({'contact_id': ObjectId(contact_id)}, {"session_id": 1, "_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_messages_session", "Getting", str(e), contact_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))
