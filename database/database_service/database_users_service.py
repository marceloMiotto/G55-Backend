from database.database_setup.mongodb import MongoCollection
from constants import C_DATE_MASK, C_ADMIN_PAGE_SIZE, C_FRONT_PAGE_SIZE, C_DELETING_ERROR, \
    C_INSERTING_ERROR, C_UPDATING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE, C_NOT_ALLOWED
from bson import ObjectId
from service.log_service import log_database
import datetime
from service.utils_service import success_to_json, error_to_json
from werkzeug.security import generate_password_hash, check_password_hash

#  TODO review APIs that returns the user id and verify if it is necessary


class DatabaseUsersService(object):

    def __init__(self):
        pass

    def get_database_users_count(self, search_word):
        try:
            mc = MongoCollection()
            col = mc.users()

            filter_statement = {"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                        {"email": {"$regex": search_word, "$options": 'i'}},
                                        {"status": {"$regex": search_word, "$options": 'i'}}
                                        ]}

            return col.count_documents(filter_statement)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_users_count", "Getting", str(e), search_word))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_users(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.users()

            filter_statement = {"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                        {"email": {"$regex": search_word, "$options": 'i'}},
                                        {"status": {"$regex": search_word, "$options": 'i'}}
                                        ]}

            return col.find(filter_statement,
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE * (start - 1)).limit(C_ADMIN_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_users", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_user(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.users()
            return col.find({"_id": ObjectId(user_id)}, {"user_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user", "Getting", str(e), ""))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_user(self, user, user_id=None):
        arguments = ""
        try:
            arguments = user
            mc = MongoCollection()
            col = mc.users()
            dt = datetime.datetime.now()
            if user_id:
                result = col.update_one({"_id": ObjectId(user_id)},
                                        {"$set": {"name": user["name"],
                                                  "last_updated_date": dt
                                                  }})

            else:
                try:
                    user["creation_date"] = dt
                    user["pwd"] = generate_password_hash(user["pwd"], method='sha256', salt_length=24)
                    r = col.insert_one(user).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_user", "Inserting", str(e), str(arguments)))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json("1")

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_user", "Updating", str(e), str(arguments)))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_user(self, user_code):
        try:
            mc = MongoCollection()
            col = mc.users()
            col.delete_one({"email": user_code})

            return success_to_json("1")

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_user", "Deleting", str(e), user_code))
            return error_to_json(C_DELETING_ERROR.format(str(e)))


    def post_database_user_enable_disable(self, user):
        try:
            mc = MongoCollection()
            col = mc.users()
            dt = datetime.datetime.now()
            result = col.update_one({"email": user["email"]},
                                    {"$set": {"status": user["status"],
                                              "last_updated_date": dt}}
                                    )

            return success_to_json("1")

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_user_enable_disable", "Updating", str(e), user))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_user_info(self, user_code):
        try:
            mc = MongoCollection()
            col = mc.users()
            return col.find({"email": user_code}, {"_id": 1, "type": 1})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_info", "Getting", str(e), user_code))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def user_database_exists(self, user_code):
        try:
            mc = MongoCollection()
            col = mc.users()
            return col.count_documents({"email": user_code})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("user_database_exists", "Getting", str(e), user_code))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def verify_database_user_credentials(self, user):
        try:
            mc = MongoCollection()
            col = mc.users()
            user_check = col.find({"email": user["email"]})
            for u in user_check:
                if check_password_hash(u["pwd"], user["pwd"]):
                    return col.find({"email": user["email"]})
                else:
                    return error_to_json(C_NOT_ALLOWED)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("verify_database_user_credentials", "Getting", str(e), user))
            return error_to_json(C_GETTING_ERROR.format(str(e)))
