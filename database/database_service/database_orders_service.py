import datetime
from database.database_setup.mongodb import MongoCollection
from service.log_service import log_database
from constants import C_ADMIN_PAGE_SIZE, C_DATE_MASK, C_INSERTING_ERROR, C_UPDATING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE, \
    C_GETTING_ERROR
from bson import ObjectId
from service.utils_service import success_to_json, error_to_json


class DatabaseOrdersService(object):
    def __init__(self):
        pass

    def get_database_orders(self, user_id, search_word, start, json_filter):
        arguments = ""
        try:
            if json_filter == "ALL" or not json_filter:
                json_filter = ["Ativo", "Cancelado", "Finalizado"]

            arguments = "search_word: " + search_word + " - start: " + str(start)

            mc = MongoCollection()
            col = mc.orders()
            return col.find({"$or": [{"number": {"$regex": search_word, "$options": 'i'}},
                                     {"buyer_name": {"$regex": search_word, "$options": 'i'}},
                                     {"status": {"$regex": search_word, "$options": 'i'}},
                                     {"freight_type": {"$regex": search_word, "$options": 'i'}}],
                             "$and": [{"user_id": ObjectId(user_id)},
                                      {"status": {"$in": json_filter}}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE * (start - 1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_orders", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_orders_count(self, user_id, search, json_filter):

        arguments = ""
        try:
            if json_filter == "ALL" or not json_filter:
                json_filter = ["Ativo", "Cancelado", "Finalizado"]
            arguments = "search: " + search
            mc = MongoCollection()
            col = mc.orders()
            return col.count_documents({"$or": [{"number": {"$regex": search, "$options": 'i'}},
                                                {"buyer_name": {"$regex": search, "$options": 'i'}},
                                                {"status": {"$regex": search, "$options": 'i'}},
                                                {"freight_type": {"$regex": search, "$options": 'i'}}
                                                ],
                                        "$and": [{"user_id": ObjectId(user_id)},
                                                 {"status": {"$in": json_filter}}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_orders_count", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def delete_database_order(self, order_id, user_id):
        arguments = ""
        try:
            arguments = "order_id: " + order_id
            mc = MongoCollection()
            col = mc.orders()
            col.delete_one({"_id": ObjectId(order_id), "user_id": ObjectId(user_id)})

            return success_to_json(order_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_order", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def get_database_order_items(self, order_id, user_id):
        try:
            mc = MongoCollection()
            col = mc.order_items()
            return col.find({"order_id": ObjectId(order_id), "user_id": ObjectId(user_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_order_items", "Getting", str(e), order_id))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def get_database_user_orders(self, user_id, search_word, start, nmessages):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + \
                        str(start) + " nmessages: " + nmessages

            if nmessages == "Y":
                nmessages = ["Y"]
            else:
                nmessages = ["Y", "N"]

            mc = MongoCollection()
            col = mc.order_items()
            return col.find({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                     {"store_name": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)},
                                      {"new_messages": {"$in": nmessages}}]},
                            {"user_id": 0}).skip(C_ADMIN_PAGE_SIZE * (start - 1)).limit(C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_orders", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_user_orders_count(self, user_id, search, nmessages):

        arguments = ""
        try:
            arguments = "user_id: " + user_id + " search: " + search + " nmessages: " + nmessages

            if nmessages == "Y":
                nmessages = ["Y"]
            else:
                nmessages = ["Y", "N"]

            mc = MongoCollection()
            col = mc.order_items()
            return col.count_documents({"$or": [{"name": {"$regex": search, "$options": 'i'}},
                                                {"store_name": {"$regex": search, "$options": 'i'}}
                                                ],
                                        "$and": [{"user_id": ObjectId(user_id)},
                                                 {"new_messages": {"$in": nmessages}}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_orders_count", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_order(self, order, user_id):
        argumnents = ""
        try:
            argumnents = order
            mc = MongoCollection()
            col = mc.orders()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            order_id = order.get("id", None)
            result = col.update_one({"_id": ObjectId(order_id), "user_id": ObjectId(user_id)},
                                    {'$set': {'number': order['number'],
                                              'buyer_name': order['buyer_name'],
                                              'freight_type': order['freight_type'],
                                              'last_updated_date': dt,
                                              "store_id": ObjectId(order["store_id"])}}
                                    )
            if result.matched_count <= 0:
                try:
                    order["creation_date"] = dt
                    order["user_id"] = ObjectId(user_id)
                    order["store_id"] = ObjectId(order["store_id"])
                    r = col.insert_one(order).inserted_id
                    return success_to_json(str(r))
                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_category", "Inserting", str(e), argumnents))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(order['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_order", "Updating", str(e), argumnents))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))


    def update_database_order_status(self, order):
        argumnents = ""
        try:
            argumnents = order
            mc = MongoCollection()
            col = mc.orders()
            dt = datetime.datetime.now()
            order_id = order.get("id", None)
            result = col.update_one({"_id": ObjectId(order_id)},
                                    {'$set': {'status': order['status'],
                                              'last_updated_date': dt}}
                                    )

            return success_to_json(order['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("update_database_order_status", "Updating", str(e), argumnents))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
