from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
from service.log_service import log_database
from constants import C_UPDATING_ERROR, C_INSERTING_ERROR, \
    C_DELETING_ERROR, C_GETTING_ERROR, C_ADMIN_PAGE_SIZE, C_FRONT_PAGE_SIZE, C_LOG_MESSAGE, C_LOG_DATE_MASK, C_DATE_MASK
import datetime
from service.utils_service import success_to_json, error_to_json
import re
from unicodedata import normalize


class DatabaseStoresService(object):

    def __init__(self):
        pass

    def get_database_stores_front(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.stores()
            if search_word != "All":
                array_statement = [{"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                            {"description": {"$regex": search_word, "$options": 'i'}}
                                            ]}]

                filter_statement = {"$and": array_statement}

            else:
                filter_statement = {}

            return col.find(filter_statement,
                            {"user_id": 0}).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_stores_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_fav_stores_front(self, user_id, fav_type):
        arguments = ""
        try:
            arguments = "type: " + fav_type
            mc = MongoCollection()
            col = mc.user_favorites()
            return col.find({'user_id': ObjectId(user_id), 'type': fav_type}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_fav_stores_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_store_front_one(self, store_code):
        arguments = ""
        try:
            arguments = "store_code: " + str(store_code)
            mc = MongoCollection()
            col = mc.stores()
            return col.find({"store_code": store_code}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_store_front_one", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))
            
    def is_store_code_unique(self, store_code):
        arguments = ""
        try:
            arguments = "store_code: " + store_code
            mc = MongoCollection()
            col = mc.stores()
            count_store_code = col.count_documents({"store_code": store_code})
            print(count_store_code)
            if count_store_code > 0:
                return True
            else:
                return False

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("is_store_code_unique", "Validating", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_store_id(self, store_code):
        arguments = ""
        try:
            arguments = "store_code: " + store_code
            mc = MongoCollection()
            col = mc.stores()
            store_id = col.find({"store_code": store_code}, {"_id": 1})
            return store_id

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_store_id", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_user_store(self, user_id):
        arguments = ""
        try:
            mc = MongoCollection()
            col = mc.stores()
            return col.find({"user_id": ObjectId(user_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_store_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_user_store(self, store, user_id):
        arguments = ""
        try:
            arguments = store
            mc = MongoCollection()
            col = mc.stores()
            dt = datetime.datetime.now()
            store_id = store.get("id", None)
            result = col.update_one({"_id": ObjectId(store_id), "user_id": ObjectId(user_id)},
                                    {"$set": {"name": store["name"],
                                              "description": store["description"],
                                              "store_code": store["store_code"],
                                              "last_updated_date": dt
                                              }})
            if result.matched_count <= 0:
                try:
                    store["creation_date"] = dt
                    store["user_id"] = ObjectId(user_id)
                    store["store_code"] = self.get_store_code_from_store_name(store["name"])
                    r = col.insert_one(store).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_user_store", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(store['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_user_store", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_store_code_from_store_name(self, store_name):
        arguments = ""
        try:
            arguments = "store_name: " + store_name
            store_code = store_name.replace("´", "")
            store_code = normalize('NFKD', store_code).encode('ASCII', 'ignore').decode('ASCII')
            store_code = re.sub('[^a-zA-Z0-9 \\\]', '', store_code).lower().replace(" ", "_").strip("_")
            return store_code

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_user_store", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_google_analytics_code(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.stores()
            return col.find({"user_id": ObjectId(user_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_google_analytics_code", "Getting", str(e), user_id))
            # TODO remove debug messages after tests
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def update_database_google_analytics_code(self, arguments, user_id):
        """
           Function to create or update the google analytics code
           Parameter: code - google analytics code
           Return Error or Success
        """
        try:
            mc = MongoCollection()
            col = mc.stores()
            dt = datetime.datetime.now()
            result = col.update_one({"user_id": ObjectId(user_id)},
                                    {'$set': {'google_analytics_code': arguments['google_analytics_code'],
                                              'last_updated_date': dt}}
                                    )
            return success_to_json(arguments['user_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("update_database_google_analytics_code", "Updating", str(e), arguments + "user_id: " + user_id))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

