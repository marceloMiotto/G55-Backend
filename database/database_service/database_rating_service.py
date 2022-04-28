import datetime
from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_FRONT_PAGE_SIZE, C_ADMIN_PAGE_SIZE, C_DATE_MASK, C_INSERTING_ERROR, C_UPDATING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE, C_GETTING_ERROR
from bson import ObjectId
from service.utils_service import success_to_json, error_to_json


class DatabaseRatingService(object):
    def __init__(self):
        pass

    def get_database_ratings(self, ref_id, start):
        arguments = ""
        try:
            arguments = "ref_id: " + ref_id + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.reviews()
            return col.find({"ref_id": ObjectId(ref_id)}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_ratings", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_ratings_count(self, ref_id):

        try:
            mc = MongoCollection()
            col = mc.reviews()
            return col.count_documents({"ref_id": ObjectId(ref_id)})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_ratings_count", "Getting", str(e), ref_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_rating(self, rating_id, user_id):
        argumnents = ""
        try:
            argumnents = "rating_id: " + rating_id
            mc = MongoCollection()
            col = mc.reviews()
            col.delete_one({"_id": ObjectId(rating_id), "user_id": ObjectId(user_id)})

            return success_to_json(rating_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_rating", "Deleting", str(e), argumnents))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def merge_database_rating(self, rating, user_id):
        argumnents = ""
        try:
            argumnents = rating
            mc = MongoCollection()
            col = mc.reviews()
            dt = datetime.datetime.now()
            rating_id = rating.get("id", None)
            result = col.update_one({"_id": ObjectId(rating_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'review': rating['review'],
                                              'rating': rating['rating'],
                                              'type': rating['rating_type'],
                                              'status': rating['status'],
                                              'store_name': rating['store_name'],
                                              'store_code': rating['store_code'],
                                              'last_updated_date': dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    rating["creation_date"] = dt
                    rating["ref_id"] = ObjectId(rating["ref_id"])
                    rating["user_id"] = ObjectId(user_id)
                    r = col.insert_one(rating).inserted_id

                    return success_to_json(str(r))
                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_rating", "Inserting", str(e), argumnents))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(rating['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_rating", "Updating", str(e), argumnents))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def update_database_rating_answer(self, rating_id, rating):
        arguments = ""
        try:
            arguments = "rating_id: " + rating_id + " rating: " + str(rating)
            mc = MongoCollection()
            col = mc.reviews()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            result = col.update_one({"_id": ObjectId(rating_id)},
                                    {'$set': {'answer_review': rating['answer_review'],
                                              'last_updated_date': dt}}
                                    )

            return success_to_json(rating_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_rating", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))





