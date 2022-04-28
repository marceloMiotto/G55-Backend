from database.database_setup.mongodb import MongoCollection
from bson import ObjectId
from service.log_service import log_database
from constants import C_UPDATING_ERROR, C_GETTING_ERROR, C_LOG_MESSAGE, C_DELETING_ERROR, C_INSERTING_ERROR
from service.utils_service import success_to_json, error_to_json


class DatabaseCartService(object):

    def __init__(self):
        pass

    def update_database_store_coupon_product_cart(self, cart_id, product_id, discount):
        arguments = ""
        try:
            arguments = "cart_id: " + cart_id + " - product_id:" + product_id + " - discount: " + str(discount)
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'_id': ObjectId(cart_id),
                            'products.product_id': ObjectId(product_id)
                            },
                           {'$set': {'products.$.discount': discount}
                            },
                           )
            return success_to_json(cart_id)

        except Exception as e:
            log_database(
                C_LOG_MESSAGE.format("update_database_store_coupon_product_cart", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def update_database_store_coupon_cart(self, cart_id, coupon_code, coupon_discount):
        arguments = ""
        try:
            arguments = "cart_id: " + cart_id + " - coupon_code:" + coupon_code + " - coupon_discount: " + str(
                coupon_discount)
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'_id': ObjectId(cart_id)
                            },
                           {'$set': {'coupon': coupon_code,
                                     'discount_value': coupon_discount}
                            },
                           )
            return success_to_json(cart_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("update_database_store_coupon_cart", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_user_cart(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            return col.find({"user_id": ObjectId(user_id)})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_cart", "Getting", str(e), user_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def get_database_user_store_cart_front(self, find_statement):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            return col.find(find_statement)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_store_cart_front", "Getting", str(e), find_statement))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def post_database_cart_product_observation_front(self, product):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'_id': ObjectId(product['cart_id']),
                            'products.product_id': ObjectId(product['product_id'])
                            },
                           {'$set': {'products.$.observations': product['observations']}
                            },
                           )
            return success_to_json(product['cart_id'])

        except Exception as e:
            log_database(
                C_LOG_MESSAGE.format("post_database_cart_product_observation_front", "Updating", str(e), product))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_coupon_front(self, coupon_code, store_id):
        arguments = ""
        try:
            arguments = "coupon_code: " + coupon_code + " - store_id: " + store_id
            mc = MongoCollection()
            col = mc.coupon()
            return col.find({'code': coupon_code,
                             'store_id': ObjectId(store_id)
                             })

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_coupon_front", "Getting", str(e), arguments))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def post_database_cart_product_gift_front(self, product):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'_id': ObjectId(product['cart_id']),
                            'products.product_id': ObjectId(product['product_id'])
                            },
                           {'$set': {'products.$.gift_flag': product['gift_flag']}
                            },
                           )
            return success_to_json(product['cart_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_cart_product_gift_front", "Updating", str(e), product))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def post_database_cart_product_quantity_front(self, product):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'_id': ObjectId(product['cart_id']),
                            'products.product_id': ObjectId(product['product_id'])
                            },
                           {'$set': {'products.$.quantity': float(product['quantity'])}
                            },
                           )
            return success_to_json(product['cart_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_cart_product_quantity_front", "Updating", str(e), product))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def get_database_user_cart_front(self, user_id):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            return col.find({'user_id': ObjectId(user_id)})
        except Exception as e:
            log_database(C_LOG_MESSAGE.format("get_database_user_cart_front", "Getting", str(e), user_id))
            return error_to_json(C_GETTING_ERROR.format(str(e)))

    def update_product(self, col, product):

        try:
            col.update_one({'user_id': ObjectId(product['user_id']),
                            'store_id': ObjectId(product['store_id'])
                            },
                           {'$push': {'products': {'product_id': ObjectId(product['product_id']),
                                                   'product_name': product['product_name'],
                                                   'product_photo': str(product['product_photo']),
                                                   'price': float(product['price']),
                                                   'quantity': float(product['quantity']),
                                                   'gift_flag': product['gift_flag'],
                                                   'gift_value': float(product['gift_value']),
                                                   'observations': product['observations'],
                                                   'category_name': product['category_name'],
                                                   'discount': float(product['discount'])}
                                      }
                            },
                           )

            return success_to_json(product['user_id'])

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("update_product", "Updating", str(e), product))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def post_database_user_cart_front(self, product):
        try:
            mc = MongoCollection()
            col = mc.user_carts()
            local_cart_id = product.get("_id", None)

            count_user_store = col.count_documents({'user_id': ObjectId(product['user_id']),
                                                    'store_id': ObjectId(product['store_id'])})

            if count_user_store > 0:

                count_products = col.count_documents({'user_id': ObjectId(product['user_id']),
                                                      'store_id': ObjectId(product['store_id']),
                                                      'products.product_id': ObjectId(product['product_id'])})

                if count_products > 0:

                    col.update_one({'user_id': ObjectId(product['user_id']),
                                    'store_id': ObjectId(product['store_id']),
                                    'products.product_id': ObjectId(product['product_id'])
                                    },
                                   {'$set': {'products.$.product_name': product['product_name'],
                                             'products.$.product_photo': str(product['product_photo']),
                                             'products.$.price': float(product['price']),
                                             'products.$.quantity': float(product['quantity']),
                                             'products.$.gift_flag': product['gift_flag'],
                                             'products.$.gift_value': float(product['gift_value']),
                                             'products.$.observations': product['observations'],
                                             'products.$.category_name': product['category_name'],
                                             'products.$.discount': float(product['discount'])
                                             }
                                    },
                                   )
                else:
                    self.update_product(col, product)

            else:  # create user cart
                print("debug2")
                print(product)
                try:
                    local_cart_id = col.insert_one({'user_id': ObjectId(product['user_id']),
                                                    'store_id': ObjectId(product['store_id']),
                                                    'status': 'Active',
                                                    'coupon': product['coupon'],
                                                    'discount_value': float(product['discount_value']),
                                                    'freight_type': product['freight_type'],
                                                    'freight_value': float(product['freight_value']),
                                                    'freight_eta': float(product['freight_eta']),
                                                    'store_code': product['store_code']}).inserted_id
                except Exception as e:
                    log_database(C_LOG_MESSAGE.format("post_database_user_cart_front", "Inserting", str(e), product))
                    return error_to_json(C_INSERTING_ERROR.format(str(e)))

                self.update_product(col, product)

            return success_to_json(str(local_cart_id))  # TODO review '{"output": "SUCCESS", "user_id": "' + product['product_id'] + '"}'

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("post_database_user_cart_front", "Updating", str(e), product))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))

    def delete_database_user_cart_store_front(self, user_id, store_id):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " - store_id: " + store_id
            mc = MongoCollection()
            col = mc.user_carts()
            col.delete_one({'user_id': ObjectId(user_id), 'store_id': ObjectId(store_id)})
            return success_to_json(user_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_user_cart_store_front", "Deleting", str(e), arguments))
            return error_to_json(C_DELETING_ERROR.format(str(e)))

    def delete_database_user_cart_product_front(self, user_id, store_id, product_id, quantity):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " - store_id: " + store_id + " - product_id: " + product_id + \
                        " - quantity: " + quantity
            mc = MongoCollection()
            col = mc.user_carts()
            col.update_one({'user_id': ObjectId(user_id),
                            'store_id': ObjectId(store_id),
                            },
                           {'$pull': {'products': {'product_id': ObjectId(product_id)}},
                            '$inc': {'total': - quantity}}
                           )
            return success_to_json(user_id)

        except Exception as e:
            log_database(C_LOG_MESSAGE.format("delete_database_user_cart_product_front", "Updating", str(e), arguments))
            return error_to_json(C_UPDATING_ERROR.format(str(e)))
