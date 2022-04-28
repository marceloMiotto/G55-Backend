from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
from service.log_service import log_database
from constants import C_ADMIN_PAGE_SIZE, C_DELETING_ERROR, C_INSERTING_ERROR, \
    C_GETTING_ERROR, C_UPDATING_ERROR, C_LOG_MESSAGE, C_DATE_MASK
from service.utils_service import success_to_json, error_to_json
import datetime


class DatabaseReviewsService(object):
    def __init__(self):
        pass

    def get_database_reviews_front(self, ref_id):
        try:
            mc = MongoCollection()
            col = mc.reviews()
            return col.find({'_id': ObjectId(ref_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_reviews_front", "Getting", str(e), ref_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_reviews(self, user_id, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.reviews()
            return col.find({"$or": [{"store_name": {"$regex": search_word, "$options": 'i'}},
                                     {"type": {"$regex": search_word, "$options": 'i'}},
                                     {"user_name": {"$regex": search_word, "$options": 'i'}},
                                     {"status": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)}]

                             },
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_reviews", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_review(self, review_id):
        try:
            mc = MongoCollection()
            col = mc.reviews()
            return col.find({"_id": ObjectId(review_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_review", "Getting", str(e), review_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_reviews_count(self, user_id, search_word):
        try:
            mc = MongoCollection()
            col = mc.reviews()
            return col.count_documents({"$or": [{"store_name": {"$regex": search_word, "$options": 'i'}},
                                                {"type": {"$regex": search_word, "$options": 'i'}},
                                                {"user_name": {"$regex": search_word, "$options": 'i'}},
                                                {"status": {"$regex": search_word, "$options": 'i'}}],
                                        "$and": [{"user_id": ObjectId(user_id)}]
                                        })
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_reviews_count", "Getting", str(e), search_word))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def insert_database_review(self, review, user_id):
        arguments = ""
        try:
            arguments = review
            mc = MongoCollection()
            col = mc.reviews()
            dt = datetime.datetime.now()
            review["creation_date"] = dt
            review["user_id"] = ObjectId(user_id)
            r = col.insert_one(review).inserted_id

            return success_to_json(str(r))

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("insert_database_review", "Inserting", str(e), arguments))
            return error_to_json(C_INSERTING_ERROR.format(str(e)))

    def delete_database_review(self, review_id, user_id):
        arguments = ""
        try:
            arguments = "review_id: " + review_id + " user_id: " + user_id
            mc = MongoCollection()
            col = mc.reviews()
            col.update_one({"_id": ObjectId(review_id), "user_id": ObjectId(user_id)},
                           {'$set': {'deleted': "Y"}})

            return success_to_json(review_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_review", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))
