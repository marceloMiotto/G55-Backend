import datetime
from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_ADMIN_PAGE_SIZE, C_DATE_MASK, C_INSERTING_ERROR, C_UPDATING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE, C_GETTING_ERROR
from bson import ObjectId
from service.utils_service import success_to_json, error_to_json


class DatabaseCategoryService(object):
    def __init__(self):
        pass

    def get_database_categories_front(self, store_id, store_code):
        arguments = "store_id: " + str(store_id) + " - store_code: " + store_code
        try:
            mc = MongoCollection()
            if store_code == "ALL":
                col = mc.categories()
                return col.find({}, {"name": 1, "type": 1})
            else:
                col = mc.products()
                categories = col.aggregate([{"$match": {"store_id": ObjectId(store_id)}}, {"$group": {"_id": "$category_id"}}])
                catg_array = []
                for c in categories:
                    catg_array.append(c["_id"])
                colc = mc.categories()
                return colc.find({"_id": {"$in": catg_array}}, {"name": 1, "type": 1})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_categories_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_categories(self, search_word, start, user_id):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.categories()
            return col.find({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                     {"type": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_categories", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_category_count(self, search):

        try:
            mc = MongoCollection()
            col = mc.categories()
            return col.count_documents({"$or": [{"name": {"$regex": search, "$options": 'i'}},
                                       {"type": {"$regex": search, "$options": 'i'}}
                                       ]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_category_count", "Getting", str(e), search))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_category(self, category_id, user_id):
        arguments = ""
        try:
            arguments = "category_id: " + str(category_id)
            mc = MongoCollection()
            col = mc.categories()
            col.delete_one({"_id": ObjectId(category_id), "user_id": ObjectId(user_id)})

            return success_to_json(category_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_category", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def merge_database_category(self, category, user_id):
        arguments = ""
        try:
            arguments = str(category)
            mc = MongoCollection()
            col = mc.categories()
            dt = datetime.datetime.now()
            category_id = category.get("id", None)
            result = col.update_one({"_id": ObjectId(category_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'name': category['name'],
                                              'type': category['type'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    category["creation_date"] = dt
                    category["user_id"] = ObjectId(user_id)
                    r = col.insert_one(category).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_category", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(category['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_category", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_category_id(self, category_name):
        arguments = ""
        try:
            arguments = "category_name: " + category_name
            mc = MongoCollection()
            col = mc.categories()
            cur_category = col.find({"name": category_name}, {"_id": 1})
            for c in cur_category:
                return c["_id"]

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_category_id", "Getting", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
