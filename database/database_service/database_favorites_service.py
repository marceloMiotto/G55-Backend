from database.database_setup.mongodb import MongoCollection
from constants import C_ADMIN_PAGE_SIZE, C_FRONT_PAGE_SIZE, C_DATE_MASK, C_INSERTING_ERROR, \
    C_UPDATING_ERROR, C_GETTING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE, C_G55
from bson import ObjectId
from service.log_service import log_database
import datetime
from service.utils_service import success_to_json, error_to_json


class DatabaseFavoritesService(object):

    def __init__(self):
        pass

    def merge_database_favorites(self, favorite, user_id):
        arguments = ""
        try:
            arguments = favorite
            mc = MongoCollection()
            col = mc.user_favorites()
            dt = datetime.datetime.now()
            result = col.update_one({"favorite_id": ObjectId(favorite["favorite_id"]),
                                     "user_id": ObjectId(user_id)},
                                    {"$set": {"last_updated_date": dt}}
                                    )
            if result.matched_count <= 0:
                try:
                    favorite["favorite_id"] = ObjectId(favorite['favorite_id'])
                    favorite["user_id"] = ObjectId(user_id)
                    favorite["creation_date"] = dt
                    r = col.insert_one(favorite).inserted_id

                    return success_to_json(str(r))

                except Exception as e:
                    log_database(
                        C_LOG_MESSAGE.format("merge_database_product_favorites", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(favorite['favorite_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_favorites", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_favorite(self, favorite_id, user_id):
        arguments = ""
        try:
            arguments = "favorite_id: " + favorite_id
            mc = MongoCollection()
            col = mc.user_favorites()
            col.delete_one({"favorite_id": ObjectId(favorite_id), "user_id": ObjectId(user_id)})

            return success_to_json(favorite_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_product_favorite", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def get_database_favorite_products(self, user_id):
        arguments = ""
        try:
            mc = MongoCollection()
            col_fav = mc.user_favorites()
            cur_fav_products = col_fav.find({"user_id": ObjectId(user_id), "type": "PRODUCT"})

            favorite_products = []
            for c in cur_fav_products:
                favorite_products.append(c['favorite_id'])

            col = mc.products()
            return col.find({"_id": {"$in": favorite_products}}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_products", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_favorite_stores(self, user_id):
        arguments = ""
        try:
            mc = MongoCollection()
            col_fav = mc.user_favorites()
            cur_fav_stores = col_fav.find({"user_id": ObjectId(user_id), "type": "STORE"})

            favorite_stores = []
            for c in cur_fav_stores:

                favorite_stores.append(c['favorite_id'])

            col = mc.stores()
            return col.find({"_id": {"$in": favorite_stores}}, {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_favorite_stores", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))