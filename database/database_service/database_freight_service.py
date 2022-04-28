from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_ADMIN_PAGE_SIZE, C_DATE_MASK, C_DELETING_ERROR, \
    C_UPDATING_ERROR, C_INSERTING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE
from bson import ObjectId
import datetime
from service.utils_service import success_to_json, error_to_json


class DatabaseFreightTypeService(object):
    def __init__(self):
        pass

    def get_database_freight_types(self, search_word, start, user_id):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.freight_types()
            return col.find({"$or": [{"name": {"$regex": search_word, "$options": 'i'}}],
                             "$and": [{"user_id": ObjectId(user_id)}]
                             },
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_freight_types", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_freight_count(self, search):
        try:
            mc = MongoCollection()
            col = mc.freight_types()
            return col.count_documents({"$or": [{"name": {"$regex": search, "$options": 'i'}}
                                                ]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_freight_count", "Getting", str(e), search))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_freight_types(self, freight_type_id, user_id):
        arguments = ""
        try:
            arguments = "freight_type_id: " + freight_type_id
            mc = MongoCollection()
            col = mc.freight_types()
            col.delete_one({"_id": ObjectId(freight_type_id), "user_id": ObjectId(user_id)})

            return success_to_json(freight_type_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_freight_types", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def merge_database_freight_type(self, freight, user_id):
        arguments = ""
        try:
            arguments = freight
            mc = MongoCollection()
            col = mc.freight_types()
            dt = datetime.datetime.now()
            freight_id = freight.get("id", None)
            result = col.update_one({"_id": ObjectId(freight_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'name': freight['name'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    freight["creation_date"] = dt
                    freight["user_id"] = ObjectId(user_id)
                    r = col.insert_one(freight).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_freight_type", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(freight['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_freight_type", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
