from database.database_setup.mongodb import MongoCollection
from constants import C_DATE_MASK, C_ADMIN_PAGE_SIZE, C_FRONT_PAGE_SIZE, C_DELETING_ERROR, \
    C_INSERTING_ERROR, C_UPDATING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE
from bson import ObjectId
from service.log_service import log_database
import datetime
from service.utils_service import success_to_json, error_to_json


class DatabaseProfileService(object):

    def __init__(self):
        pass

    def get_database_artists_all_front(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.profiles()

            if search_word != "All":
                array_statement = [{"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                            {"last_name": {"$regex": search_word, "$options": 'i'}}
                                            ]}, {"type": "ARTIST"}]

                filter_statement = {"$and": array_statement}

            else:
                filter_statement = {"type": "ARTIST"}

            return col.find(filter_statement, {"name": 1,
                                               "last_name": 1,
                                               "store_code": 1,
                                               "photo": 1}).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_artists_all_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_artists_one_front(self, profile_id):
        try:
            mc = MongoCollection()
            col = mc.profiles()
            return col.find({"_id": ObjectId(profile_id)}, {"user_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_artists_one_front", "Getting", str(e), profile_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_profile(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.profiles()
            return col.find({"user_id": ObjectId(user_id)}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_profile", "Getting", str(e), "Get Profile"))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_profile(self, profile, user_id):
        arguments = ""
        try:
            arguments = profile
            mc = MongoCollection()
            col = mc.profiles()
            dt = datetime.datetime.now()
            profile_id = profile.get("id", None)
            result = col.update_one({"_id": ObjectId(profile_id), "user_id": ObjectId(user_id)},
                                    {"$set": {"name": profile["name"],
                                              "last_name": profile["last_name"],
                                              "cpf": profile["cpf"],
                                              "cell": profile["cell"],
                                              "birthday": profile["birthday"],
                                              "history": profile["history"],
                                              "photo": profile["photo"],
                                              "last_updated_date": dt,
                                              "addresses": profile["addresses"],
                                              "main_address": profile["main_address"]
                                              }})

            if result.matched_count <= 0:
                try:
                    profile["creation_date"] = dt
                    profile["user_id"] = ObjectId(user_id)
                    r = col.insert_one(profile).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_profile", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(profile['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_profile", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_profile(self, profile_id, user_id):
        arguments = ""
        try:
            arguments ="profile_id: " + profile_id
            mc = MongoCollection()
            col = mc.profiles()
            col.delete_one({"_id": ObjectId(profile_id), "user_id": ObjectId(user_id)})

            return success_to_json(profile_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_profile", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))
