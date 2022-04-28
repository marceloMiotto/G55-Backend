from database.database_service.database_cart_service import DatabaseCartService
from bson.json_util import dumps
from bson import ObjectId
from service.log_service import log
import datetime
from service.log_service import log
from service.utils_service import error_to_json
from constants import C_LOG_MESSAGE, C_HANDLE_ERROR, C_SUCCESS


class CartServices(object):

    def __init__(self):
        pass

    def update_user_cart(self, product):
        try:
            total_values = {}
            cart = DatabaseCartService()
            cart_total = 0
            result = cart.get_database_user_cart(user_id=product['user_id'])
            cart_sub_total = 0
            sub_total = 0
            freight_value = 0
            cart_freight_value = 0
            discount_value = 0
            cart_discount_value = 0
            for r in result:
                freight_value += r['freight_value']
                discount_value += r['discount_value']
                if r['_id'] == ObjectId(product['cart_id']):
                    cart_freight_value = r['freight_value']
                    cart_discount_value += r['discount_value']

                for item in r['products']:
                    print(item)
                    sub_total += item['price'] * item['quantity']
                    cart_discount_value += item['discount']
                    discount_value += item['discount']

                    if item['gift_flag'] == "Y":
                        sub_total += item['gift_value']

                    if r['_id'] == ObjectId(product['cart_id']):
                        cart_sub_total += item['price'] * item['quantity']
                        if item['gift_flag'] == "Y":
                            cart_sub_total += item['gift_value']

                if r['_id'] == ObjectId(product['cart_id']):
                    total_values['sub_total'] = cart_sub_total
                    total_values['store_discount'] = cart_discount_value
                    total_values['store_total'] = (cart_sub_total + cart_freight_value) - cart_discount_value

                cart_total += (sub_total + freight_value) - discount_value

                total_values['cart_total'] = cart_total

                return total_values

        except Exception as e:
            log(C_LOG_MESSAGE.format("update_user_cart", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_reset_user_cart_coupon(self, user_id):

        try:
            cart = DatabaseCartService()
            user_cart = cart.get_database_user_cart(user_id=user_id)
            print(user_cart)
            for u in user_cart:
                print(u)

                cart.update_database_store_coupon_cart(cart_id=u['_id'],
                                                       coupon_code="",
                                                       coupon_discount=0)

                for c in u['products']:

                    cart.update_database_store_coupon_product_cart(cart_id=u['_id'],
                                                                   product_id=c['product_id'],
                                                                   discount=0)

            return C_SUCCESS

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_reset_user_cart_coupon", "Handling", str(e), user_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_cart_coupon_front(self, product):
        try:
            cart = DatabaseCartService()
            coupon = cart.get_database_coupon_front(coupon_code=product['coupon_code'],
                                                    store_id=product['store_id'])

            print("debug1")

            # coupon validation
            # Valid Date
            for c in coupon:
                # Validate Quantity  ??? TODO verify how to define the quantity

                print("debug2")
                if c['start_date'] <= datetime.datetime.now() <= c['end_date']:
                    pass
                else:
                    return dumps({"result": "ERROR - Invalid Date"})

                find_statement = {"user_id": ObjectId("5ccb1b5faee7b844e89368d2")}  # set a dummy user
                if c['type'] == "STORE":

                    find_statement = {'$and': [{'user_id': ObjectId(product['user_id'])},
                                               {'store_id': ObjectId(product['store_id'])},
                                               {'products.product_name': {'$nin': c['products']}},
                                               {'products.category_name': {'$nin': c['categories']}}
                                               ]
                                    }

                if c['type'] == "CATEGORY":
                    print("debug3")
                    print(c['products'])
                    print(c['categories'])

                    find_statement = {'$and': [{'user_id': ObjectId(product['user_id'])},
                                               {'store_id': ObjectId(product['store_id'])},
                                               {'products.product_name': {'$nin': c['products']}},
                                               {'products.category_name': {'$in': c['categories']}}
                                               ]
                                    }

                if c['type'] == "PRODUCT":
                    print("debug4")
                    find_statement = {'$and': [{'user_id': ObjectId(product['user_id'])},
                                               {'store_id': ObjectId(product['store_id'])},
                                               {'products.product_name': {'$in': c['products']}}
                                               ]
                                      }

                products_cart = cart.get_database_user_store_cart_front(find_statement=find_statement)
                discount_value = 0
                for item in products_cart:
                    for p in item['products']:
                        if c['discount_type'] == 'PERCENT':
                            # update user_cart
                            discount_value += ((p['price'] * p['quantity']) * c['discount_value'])/100
                            cart.update_database_store_coupon_product_cart(cart_id=item['_id'],
                                                                           product_id=p['product_id'],
                                                                           discount=discount_value)
                        else:
                            cart.update_database_store_coupon_cart(cart_id=item['_id'],
                                                                   coupon_code=c['code'],
                                                                   coupon_discount=c['discount_value'])

            total_values = self.update_user_cart(product=product)

            return dumps(total_values)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_cart_coupon_front", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_cart_product_gift_front(self, product):
        try:
            cart = DatabaseCartService()
            result = cart.post_database_cart_product_gift_front(product=product)
            if result == C_SUCCESS:
                result = self.update_user_cart(product=product)

            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_cart_product_gift_front", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_cart_product_quantity_front(self, product):
        try:
            cart = DatabaseCartService()
            result = cart.post_database_cart_product_quantity_front(product=product)
            if result == "SUCCESS":
                if product['coupon_code']:
                    result = self.post_cart_coupon_front(product=product)
                    return result
                else:
                    result = self.update_user_cart(product=product)
                    return dumps(result)
        except Exception as e:
            log(C_LOG_MESSAGE.format("post_cart_product_quantity_front", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_cart_product_observation_front(self, product):
        try:
            cart = DatabaseCartService()
            result = cart.post_database_cart_product_observation_front(product=product)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_cart_product_observation_front", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def get_user_cart_front(self, user_id):
        try:
            cart = DatabaseCartService()
            result = self.post_reset_user_cart_coupon(user_id=user_id)
            result = cart.get_database_user_cart_front(user_id=user_id)
            return dumps(result)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_user_cart_front", "Handling", str(e), user_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def post_user_cart_front(self, product):
        try:
            cart = DatabaseCartService()
            result = cart.post_database_user_cart_front(product=product)
            return result
        except Exception as e:
            log(C_LOG_MESSAGE.format("post_user_cart_front", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def delete_user_cart_store_front(self, user_id, store_id):
        try:
            arguments = "user_id: " + user_id + " - store_id: " + store_id
            cart = DatabaseCartService()
            result = cart.delete_database_user_cart_store_front(user_id=user_id,
                                                                store_id=store_id)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_user_cart_store_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))

    def delete_user_cart_product_front(self, user_id, store_id, product_id, quantity):
        try:
            arguments = "user_id: " + user_id + " - store_id: " + store_id + \
                        "product_id: " + product_id + " - quantity: " + quantity
            cart = DatabaseCartService()
            result = cart.delete_database_user_cart_product_front(user_id=user_id,
                                                                  store_id=store_id,
                                                                  product_id=product_id,
                                                                  quantity=quantity)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_user_cart_product_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))))
