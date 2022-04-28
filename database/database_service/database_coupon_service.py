from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_ADMIN_PAGE_SIZE, C_DATE_MASK, C_UPDATING_ERROR, \
    C_INSERTING_ERROR, C_DELETING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE
from bson import ObjectId
import datetime
from service.utils_service import success_to_json, error_to_json


class DatabaseCouponService(object):

    def __init__(self):
        pass

    def get_database_coupon(self, coupon_id, user_id):
        arguments = ""
        try:
            arguments = "coupon_id: " + coupon_id
            mc = MongoCollection()
            col = mc.coupons()
            return col.find({"_id": ObjectId(coupon_id), "user_id": ObjectId(user_id)},
                            {"user_id": 0})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_coupon", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_coupon(self, coupon, user_id):
        arguments = ""
        try:
            arguments = coupon
            mc = MongoCollection()
            col = mc.coupons()
            dt = datetime.datetime.now()
            coupon_id = coupon.get("_id", None)
            result = col.update_one({"_id": ObjectId(coupon_id), "user_id": ObjectId(user_id)},
                                    {"$set": {"store_id": ObjectId(coupon["store_id"]),
                                              "code": coupon["code"],
                                              "quantity": coupon["quantity"],
                                              "type": coupon["type"],
                                              "discount_type": coupon["discount_type"],
                                              "discount_value": coupon["discount_value"],
                                              "last_updated_date": dt,
                                              "products": coupon["products"],
                                              "categories": coupon["categories"],
                                              "start_date": coupon["start_date"],
                                              "end_date": coupon["end_date"]
                                              }}
                                    )
            if result.matched_count <= 0:
                try:
                    coupon["creation_date"] = dt
                    coupon["store_id"] = ObjectId(coupon["store_id"])
                    coupon["user_id"] = ObjectId(user_id)
                    r = col.insert_one(coupon).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_coupon", "Inserting", str(e), arguments))
                    print(str(e))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(coupon['_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_coupon", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_coupon(self, coupon_id, user_id):
        arguments = ""
        try:
            arguments = "coupon_id: " + coupon_id
            mc = MongoCollection()
            col = mc.coupons()
            col.delete_one({"_id": ObjectId(coupon_id), "user_id": ObjectId(user_id)})

            return success_to_json(coupon_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_coupon", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def get_database_coupon_count(self, user_id,  search):
        arguments = ""
        try:
            arguments = " search: " + search
            mc = MongoCollection()
            col = mc.coupons()
            return col.count_documents({"$or": [{"code": {"$regex": search, "$options": 'i'}}],
                                        "$and": [{"user_id": ObjectId(user_id)}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_coupon_count", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_coupons(self, user_id, search_word, start):
        arguments = ""
        try:
            arguments = " search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.coupons()
            return col.find({"$or": [{"code": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE*(start-1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_coupons", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def post_database_coupon_enable_disable(self, coupon, user_id):
        arguments = ""
        try:
            arguments = coupon
            mc = MongoCollection()
            col = mc.coupons()
            dt = datetime.datetime.now()
            result = col.update_one({"_id": ObjectId(coupon['id']), "user_id": ObjectId(user_id)},
                                    {"$set": {"status": coupon["status"],
                                              "last_updated_date": dt}}
                                    )

            return success_to_json(coupon['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_coupon_enable_disable", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def cancel_database_coupon(self, coupon, user_id):
        arguments = ""
        try:
            arguments = coupon
            mc = MongoCollection()
            col = mc.coupons()
            dt = datetime.datetime.now()
            result = col.update_one({"_id": ObjectId(coupon['id']), "user_id": ObjectId(user_id)},
                                    {"$set": {"status": "Cancelado",
                                              "reason_to_cancel": coupon['reason_to_cancel'],
                                              "last_updated_date": dt}}
                                    )

            return success_to_json(coupon['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_coupon_enable_disable", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
