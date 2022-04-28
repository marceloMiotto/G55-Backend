from database.database_setup.mongodb import MongoCollection
from constants import C_ADMIN_PAGE_SIZE, C_FRONT_PAGE_SIZE, C_DATE_MASK, C_INSERTING_ERROR, \
    C_UPDATING_ERROR, C_GETTING_ERROR, C_DELETING_ERROR, C_LOG_MESSAGE, C_G55
from bson import ObjectId
from service.log_service import log_database
import datetime
from service.utils_service import success_to_json, error_to_json
from service.category_service import CategoryServices


class DatabaseProductService(object):

    def __init__(self):
        pass

    def get_database_profile_products_front(self, profile_id):
        try:

            mc = MongoCollection()
            col = mc.products()
            return col.find({"profile_id": ObjectId(profile_id)}, {"name": 1, "photo": 1, "store_code": 1}).limit(5)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_profile_products_front", "Getting", str(e), profile_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_products_front(self, store_id, store_code, start):

        arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + " - start: " + str(start)
        try:

            mc = MongoCollection()
            col = mc.products()
            if store_code == C_G55:
                where_st = {}
            else:
                where_st = {"store_id": ObjectId(store_id)}

            return col.find(where_st, {'name': 1,
                                       'photo': 1,
                                       'value': 1,
                                       'discount': 1,
                                       'store_id': 1,
                                       'gift_value': 1,
                                       'category_id': 1
                                       }).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_products_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_front_one(self, product_id):
        try:
            mc = MongoCollection()
            col = mc.products()
            return col.find({'_id': ObjectId(product_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_front_one", "Getting", str(e), product_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_photos_front(self, product_id):
        try:
            mc = MongoCollection()
            col = mc.product_photos()
            return col.find({'product_id': ObjectId(product_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_photos_front", "Getting", str(e), product_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_colors_front(self, product_id):
        try:
            mc = MongoCollection()
            col = mc.product_colors()
            return col.find({'product_id': ObjectId(product_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_colors_front", "Getting", str(e), product_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_colors_front_one(self, color_id):
        try:
            mc = MongoCollection()
            col = mc.product_colors()
            return col.find({'_id': ObjectId(color_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_colors_front_one", "Getting", str(e), color_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_product_category_match(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            if store_code == C_G55:
                if search_type == "CATEGORY":
                    cat = CategoryServices()
                    category_id = cat.get_category_id(category_name=search_word)
                    return {"$match": {"category_id": ObjectId(category_id)}}
                else:
                    return {"$match": {"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                               {"short_description": {"$regex": search_word, "$options": 'i'}}
                                               ]}}

            else:
                if search_type == "CATEGORY":
                    return {"$match": {"category_name": search_word, "store_id": ObjectId(store_id)}}
                else:
                    return {"$match": {"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                               {"short_description": {"$regex": search_word, "$options": 'i'}}
                                               ], "store_id": ObjectId(store_id)}}


        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_product_category_match", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_categories_front(self, store_id, category_id, store_code, category_name, start):
        arguments = ""
        try:
            arguments = "store_id:" + str(store_id) + " - category_id: " + str(category_id) + \
                        " - store_code:" + store_code + \
                        " - category_name: " + category_name + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.products()
            if store_code == C_G55:
                where_st = {"category_id": ObjectId(category_id)}
            else:
                where_st = {"store_id": ObjectId(store_id), "category_id": ObjectId(category_id)}

            return col.find(where_st).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_categories_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_search_front(self, store_id, store_code, search_word, start):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.products()
            if store_code == C_G55:
                where_st = {"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                    {"short_description": {"$regex": search_word, "$options": 'i'}}
                                    ]}
            else:
                where_st = {"store_id": ObjectId(store_id),
                            "$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                    {"short_description": {"$regex": search_word, "$options": 'i'}}
                                    ]
                            }

            return col.find(where_st).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_search_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_deliver_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            mc = MongoCollection()
            col = mc.products()
            result = col.aggregate([self.get_product_category_match(store_id=store_id,
                                                                    store_code=store_code,
                                                                    search_word=search_word,
                                                                    search_type=search_type),
                                    {"$unwind": "$deliver"},
                                    {"$group": {"_id": "$deliver",
                                                "count": {"$sum": 1},
                                                }}
                                    ])

            return result

        except Exception as e:
            log_database(
                C_LOG_MESSAGE.format("get_database_product_deliver_filter_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_category_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            mc = MongoCollection()
            col = mc.products()
            result = col.aggregate([self.get_product_category_match(store_id=store_id,
                                                                    store_code=store_code,
                                                                    search_word=search_word,
                                                                    search_type=search_type),
                                    {"$group": {"_id": "$category_name",
                                                "count": {"$sum": 1},
                                                }}
                                    ])

            return result

        except Exception as e:
            log_database(
                C_LOG_MESSAGE.format("get_database_product_category_filter_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_public_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            mc = MongoCollection()
            col = mc.products()
            result = col.aggregate([self.get_product_category_match(store_id=store_id,
                                                                    store_code=store_code,
                                                                    search_word=search_word,
                                                                    search_type=search_type),
                                    {"$unwind": "$public"},
                                    {"$group": {"_id": "$public",
                                                "count": {"$sum": 1},
                                                }}
                                    ])

            return result

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_public_filter_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_price_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code" + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            mc = MongoCollection()
            col = mc.products()
            result = col.aggregate([self.get_product_category_match(store_id=store_id,
                                                                    store_code=store_code,
                                                                    search_word=search_word,
                                                                    search_type=search_type),
                                    {"$group": {"_id": "$category_name",
                                                "max_price": {"$max": "$value"},
                                                "min_price": {"$min": "$value"},

                                                }}
                                    ])

            return result

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_price_filter_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_state_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " -search_word: " + search_word + " - search_type: " + search_type
            mc = MongoCollection()
            col = mc.products()
            result = col.aggregate([self.get_product_category_match(store_id=store_id,
                                                                    store_code=store_code,
                                                                    search_word=search_word,
                                                                    search_type=search_type),
                                    {"$group": {"_id": {"state": "$state_name",
                                                        "code": "$state_code"},
                                                "count": {"$sum": 1}}}
                                    ])

            return result

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_state_filter_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_products_filtered_front(self, store_id, store_code, search_word, search_type, json_filter, start):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type + \
                        " - json_filter: " + str(json_filter) + " - start: " + str(start)

            print(json_filter)

            if search_type == "CATEGORY":
                cat = CategoryServices()
                category_id = cat.get_category_id(category_name=search_word)
                array_statement = [{'category_id': ObjectId(category_id)}]
            else:
                array_statement = [{"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                            {"short_description": {"$regex": search_word, "$options": 'i'}}
                                            ]}]

            array_statement.append({"value": {"$gte": float(json_filter['min_price'])}})
            array_statement.append({"value": {"$lte": float(json_filter['max_price'])}})
            if json_filter['public']:
                array_statement.append({"public": {"$all": json_filter['public']}})

            if json_filter['category']:
                category_filter = []
                cat = CategoryServices()
                for cat in json_filter['category']:
                    category_filter.append(cat.get_category_id(cat['name']))

                array_statement.append({"category_name": {"$all": category_filter}})

            if json_filter['deliver']:
                array_statement.append({"deliver": {"$all": json_filter['deliver']}})

            if json_filter['state']:
                array_statement.append({"state_name": {"$in": json_filter['state']}})

            if store_code != C_G55:
                array_statement.append({"store_code": store_code})

            filter_statement = {"$and": array_statement}

            order_statement = [("name", 1)]

            if json_filter['order'] == "Novo":
                order_statement = [("creation_date", -1)]

            if json_filter['order'] == "Mais caros":
                order_statement = [("value", -1)]

            if json_filter['order'] == "Mais baratos":
                order_statement = [("value", 1)]

            print(filter_statement)

            mc = MongoCollection()
            col = mc.products()
            return col.find(filter_statement).sort(order_statement).skip(C_FRONT_PAGE_SIZE * (start - 1)).limit(C_FRONT_PAGE_SIZE)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_products_filtered_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    # TODO review all logs to include the parameters as well
    def get_database_product(self, product_id, user_id):
        arguments = ""
        try:
            arguments = "product_id: " + product_id
            mc = MongoCollection()
            col = mc.products()
            return col.find({"_id": ObjectId(product_id), "user_id": ObjectId(user_id)})

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_photos(self, product_id, user_id):
        try:
            mc = MongoCollection()
            col = mc.product_photos()
            return col.find({"product_id": ObjectId(product_id), "user_id": ObjectId(user_id)},
                            {"user_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_photos", "Getting", str(e), product_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_product_colors(self, product_id, user_id):
        try:
            mc = MongoCollection()
            col = mc.product_colors()
            return col.find({"product_id": ObjectId(product_id), "user_id": ObjectId(user_id)},
                            {"user_id": 0})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_product_colors", "Getting", str(e), product_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_products_count(self, user_id, search_word):
        arguments = ""
        try:
            arguments = "search_word: " + search_word
            mc = MongoCollection()
            col = mc.products()
            return col.count_documents({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                                {"category": {"$regex": search_word, "$options": 'i'}},
                                                {"description": {"$regex": search_word, "$options": 'i'}},
                                                {"details": {"$regex": search_word, "$options": 'i'}},
                                                {"tags": {"$regex": search_word, "$options": 'i'}}
                                                ],
                                        "$and": [{"user_id": ObjectId(user_id)}]})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_products_count", "Getting", str(e), arguments))
            print(str(e))  # TODO review all prints
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_products(self, user_id, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            mc = MongoCollection()
            col = mc.products()
            return col.find({"$or": [{"name": {"$regex": search_word, "$options": 'i'}},
                                     {"description": {"$regex": search_word, "$options": 'i'}},
                                     {"details": {"$regex": search_word, "$options": 'i'}},
                                     {"tags": {"$regex": search_word, "$options": 'i'}}
                                     ],
                             "$and": [{"user_id": ObjectId(user_id)}]}).skip(C_ADMIN_PAGE_SIZE * (start - 1)).limit(
                C_ADMIN_PAGE_SIZE)
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_products", "Getting", str(e), arguments))
            print(str(e))  # TODO review all prints
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def merge_database_product(self, product, user_id):
        arguments = ""
        try:
            arguments = product
            mc = MongoCollection()
            col = mc.products()
            dt = datetime.datetime.now()
            product_id = product.get("id", None)
            result = col.update_one({"_id": ObjectId(product_id), "user_id": user_id},
                                    {"$set": {"name": product["name"],
                                              "store_id": ObjectId(product["store_id"]),
                                              "photo": product["photo"],
                                              "discount": product["discount"],
                                              "value": product["value"],
                                              "short_description": product["short_description"],
                                              "ratings_count": product["ratings_count"],
                                              "reviews_count": product["reviews_count"],
                                              "details_features": product["details_features"],
                                              "color_flag": product["color_flag"],
                                              "category_id": ObjectId(product["category_id"]),
                                              "public": product["public"],
                                              "deliver": product["deliver"],
                                              "state_name": product["state_name"],
                                              "state_code": product["state_code"],
                                              "city": product["city"],
                                              "tags": product["tags"],
                                              "last_updated_date": dt,
                                              "description": product["description"],
                                              "details": product["details"],
                                              "width": product["width"],
                                              "height": product["height"],
                                              "weight": product["weight"],
                                              "length": product["length"],
                                              "stock_quantity": product["stock_quantity"],
                                              "gift_flag": product["gift_flag"],
                                              "gift_value": product["gift_value"],
                                              "production_term": product["production_term"],
                                              "status": product["status"]
                                              }}
                                    )
            if result.matched_count <= 0:
                try:
                    product["creation_date"] = dt
                    product["user_id"] = ObjectId(user_id)
                    product["store_id"] = ObjectId(product["store_id"])
                    product["category_id"] = ObjectId(product["category_id"])
                    r = col.insert_one(product).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("merge_database_product", "Inserting", str(e), arguments))
                    return C_INSERTING_ERROR

            return success_to_json(product['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_product", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def merge_database_product_photos(self, product_photos, user_id):
        arguments = ""
        try:
            arguments = product_photos
            mc = MongoCollection()
            col = mc.product_photos()
            result = col.update_one({"product_id": ObjectId(product_photos['product_id']), "user_id": ObjectId(user_id)},
                                    {"$set": {"photos": product_photos["photos"]}}
                                    )
            if result.matched_count <= 0:
                try:
                    product_photos["product_id"] = ObjectId(product_photos['product_id'])
                    product_photos["user_id"] = ObjectId(user_id)
                    r = col.insert_one(product_photos).inserted_id
                    return success_to_json(str(r))

                except Exception as e:
                    log_database(
                        C_LOG_MESSAGE.format("merge_database_product_photos", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(product_photos['product_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_product_photos", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def merge_database_product_colors(self, product_colors, user_id):
        arguments = ""
        try:
            arguments = product_colors
            mc = MongoCollection()
            col = mc.product_colors()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            result = col.update_one({"product_id": ObjectId(product_colors['product_id']),
                                     "color_name": product_colors["color_name"],
                                     "user_id": ObjectId(user_id)},
                                    {"$set": {"photos": product_colors["photos"],
                                              "sizes": product_colors["sizes"]}}
                                    )
            if result.matched_count <= 0:
                try:
                    product_colors["product_id"] = ObjectId(product_colors['product_id'])
                    product_colors["user_id"] = ObjectId(user_id)
                    col.insert_one(product_colors)
                except Exception as e:
                    log_database(
                        C_LOG_MESSAGE.format("merge_database_product_colors", "Inserting", str(e), arguments))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

            return success_to_json(product_colors['product_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("merge_database_product_colors", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_product(self, product_id, user_id):
        arguments = ""
        try:
            arguments = "product_id: " + product_id
            mc = MongoCollection()
            col = mc.products()
            col.delete_one({"_id": ObjectId(product_id), "user_id": ObjectId(user_id)})

            return success_to_json(product_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_product", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def delete_database_product_photos(self, product_id, user_id):
        arguments = ""
        try:
            arguments = "product_id: " + product_id
            mc = MongoCollection()
            col = mc.product_photos()
            col.delete_one({"product_id": ObjectId(product_id), "user_id": ObjectId(user_id)})

            return success_to_json(product_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_product_photos", "Deleting", str(e), product_id))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def delete_database_product_colors(self, product_id, user_id):
        arguments = ""
        try:
            arguments = "product_id: " + product_id
            mc = MongoCollection()
            col = mc.product_colors()
            col.delete_one({"product_id": ObjectId(product_id), "user_id": ObjectId(user_id)})

            return success_to_json(product_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_product_colors", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def post_database_product_sold_off(self, product, user_id):
        arguments = ""
        try:
            arguments = product
            mc = MongoCollection()
            col = mc.products()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            result = col.update_one({"_id": ObjectId(product['id']), "user_id": ObjectId(user_id)},
                                    {"$set": {"sold_off": product["sold_off"],
                                              "last_updated_date": dt}}
                                    )

            return success_to_json(product['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_product_sold_off", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def post_database_product_enable_disable(self, product, user_id):
        arguments = ""
        try:
            arguments = product
            mc = MongoCollection()
            col = mc.products()
            dt = C_DATE_MASK.format(datetime.datetime.now())
            result = col.update_one({"_id": ObjectId(product['id']), "user_id": ObjectId(user_id)},
                                    {"$set": {"status": product["status"],
                                              "last_updated_date": dt}}
                                    )

            return success_to_json(product['id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_product_enable_disable", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))


