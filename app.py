from flask import Flask, request, jsonify, session
from flask_cors import CORS
from service.analytics_service import AnalyticsServices
from service.vacation_notice_service import VacationNoticeServices
from service.freight_service import FreightServices
from service.category_service import CategoryServices
from service.complaints_service import ComplaintServices
from service.standard_message_service import StandardMessageService
from service.product_service import ProductServices
from service.banners_service import BannersServices
from service.cart_service import CartServices
from service.stores_service import StoresServices
from service.review_service import ReviewServices
from service.messages_service import MessageServices
from service.profile_service import ProfileServices
from service.newsletter_service import NewsletterServices
from service.contact_service import ContactServices
from service.coupon_service import CouponServices
from service.users_service import UsersServices
from service.orders_service import OrdersServices
from service.rating_service import RatingServices
from service.session_service import SessionServices
from service.favorites_service import FavoritesServices
from functools import wraps
import os
from constants import C_TOKEN_SECRET_KEY
import jwt
import json

SECRET_KEY = os.urandom(24)
app = Flask(__name__)
CORS(app)
app.secret_key = SECRET_KEY

#  TODO verify the admin action how to validate the token
#  TODO every new STORE should be created with all default photos and images


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.args.get('key')
        print("debug 1.1")
        print(key)
        if not key:
            print("debug 1.2 - Error not token")
            return jsonify({"message": "Token is missing!"})

        try:
            data = jwt.decode(key, C_TOKEN_SECRET_KEY)
            print(str(data))
            session["token"] = key
            print(key)
            session["user_id"] = data["user_id"]
            print("debug session user id")
            print(session["user_id"])

        except Exception as e:
            print(str(e))
            return jsonify({"message": "Token is invalid"})

        return f(*args, **kwargs)

    return decorated


def get_token_data(token):
    return jwt.decode(token, C_TOKEN_SECRET_KEY)


def get_store_id(store_code):
    store = StoresServices()
    result = store.get_store_id(store_code=store_code)
    for r in result:
        return r["_id"]


def get_category_id(category_name):
    cat = CategoryServices()
    return cat.get_category_id(category_name=category_name)


def get_user_id():
    return session["user_id"]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webapi/g55_session', methods=['GET'])
@token_required
def get_session():
    """Handle the get request"""
    print("debug156")
    session_service = SessionServices()
    result = session_service.get_session()
    return jsonify(result)


@app.route('/webapi/google_analytics', methods=['GET', 'POST'])
@token_required
def google_analytics():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        analytics = AnalyticsServices()
        result = analytics.merge_google_analytics_code(analytics=content,
                                                       user_id=get_user_id())
        return jsonify(result)
    else:
        """Handle the get request"""
        analytics = AnalyticsServices()
        result = analytics.get_google_analytics_code(user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/analytics', methods=['GET', 'POST'])
@token_required
def custom_analytics():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        analytics = AnalyticsServices()
        result = analytics.merge_custom_analytics(custom_analytics=content,
                                                  user_id=get_user_id())
        return jsonify(result)
    else:
        """Handle the get request"""
        print("debug apis ")
        analytics = AnalyticsServices()
        result = analytics.get_custom_analytics_flag(user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/vacation_notice', methods=['GET', 'POST'])
@token_required
def vacation_notice():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        vacation = VacationNoticeServices()
        result = vacation.merge_vacation_message(vacation_notice=content,
                                                 user_id=get_user_id())
        return jsonify(result)

    else:
        """Handle the get request"""
        print("debug apis ")
        vacation = VacationNoticeServices()
        result = vacation.get_vacation_message(user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/freight_type', methods=['GET', 'POST'])
@token_required
def freight_type():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        freight = FreightServices()
        result = freight.merge_freight_type(freight=content,
                                            user_id=get_user_id())
        return jsonify(result)

    else:
        """Handle the get request"""
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)

        freight = FreightServices()
        result = freight.get_freight_types(total_records=total_records,
                                           page=page,
                                           search=search,
                                           user_id=get_user_id()
                                           )
        print(result)
        return jsonify(result)


@app.route('/webapi/freight_type/<string:freight_type_id>', methods=['DELETE'])
@token_required
def delete_freight_type(freight_type_id):
    """Handle the delete request"""
    # Call the function tho handle the delete
    freight = FreightServices()
    result = freight.delete_freight_type(freight_type_id=freight_type_id,
                                         user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/categories', methods=['GET'])
@token_required
def category_front():
    """Handle the get request"""
    print("debug categories ")
    store_code = request.args.get("sc", default="ALL", type=str)
    cat = CategoryServices()
    result = cat.get_categories_front(store_id=get_store_id(store_code=store_code),
                                      store_code=store_code)
    print(result)
    return jsonify(result)


@app.route('/webapi/category', methods=['GET', 'POST', 'DELETE'])
@token_required
def category():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        cat = CategoryServices()
        result = cat.merge_category(category=content,
                                    user_id=get_user_id())
        return jsonify(result)

    elif request.method == 'DELETE':
        """Handle the delete request"""
        category_id = request.args.get("id", default=1, type=str)
        # Call the function tho handle the delete
        cat = CategoryServices()
        result = cat.delete_category(category_id=category_id,
                                     user_id=get_user_id()
                                     )
        return jsonify(result)

    else:
        """Handle the get request"""
        print("debug apis ")
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        cat = CategoryServices()
        result = cat.get_categories(total_records=total_records,
                                    page=page,
                                    search=search,
                                    user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/coupons', methods=['GET'])
@token_required
def coupons():
    total_records = request.args.get("total_records", default=0, type=int)
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search", default="", type=str)
    coupon = CouponServices()
    result = coupon.get_coupons(user_id=get_user_id(),
                                total_records=total_records,
                                page=page,
                                search=search)
    return jsonify(result)


@app.route('/webapi/coupon/<string:coupon_id>', methods=['GET'])
@token_required
def coupon_one(coupon_id):
    coupon = CouponServices()
    result = coupon.get_coupon(coupon_id=coupon_id,
                               user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/coupon_enable_disable', methods=['POST'])
@token_required
def coupon_enable_disable():
    """Handle the get request"""
    content = request.get_json(silent=True)
    coupon_service = CouponServices()
    result = coupon_service.post_coupon_enable_disable(coupon=content,
                                                       user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/coupon_cancel', methods=['POST'])
@token_required
def coupon_cancel():
    """Handle the get request"""
    content = request.get_json(silent=True)
    coupon_service = CouponServices()
    result = coupon_service.coupon_cancel(coupon=content,
                                          user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/coupon', methods=['POST'])
@token_required
def merge_coupon():
    """Handle the get request"""
    content = request.get_json(silent=True)
    coupon_service = CouponServices()
    result = coupon_service.post_coupon(coupon=content,
                                        user_id=get_user_id())
    return jsonify(result)



@app.route('/webapi/rating', methods=['GET', 'POST'])
@token_required
def rating():

    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        # Call the function tho handle the insert or update
        rating_service = RatingServices()
        result = rating_service.merge_rating(rating=content,
                                             user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/rating/<string:rating_id>', methods=['POST'])
@token_required
def rating_answer(rating_id):

    print(rating_id)

    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        # Call the function tho handle the insert or update
        rating_service = RatingServices()
        result = rating_service.update_rating_review(rating_id,
                                                     rating=content,
                                                     user_id=get_user_id()
                                                     )
        return jsonify(result)


@app.route('/webapi/complaints', methods=['GET', 'POST'])
@token_required
def complaints():
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        comp = ComplaintServices()
        result = comp.insert_complaint(complaint=content,
                                       user_id=get_user_id())
        return jsonify(result)

    else:
        """Handle the get request"""
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        print(total_records)
        print(page)
        print(search)

        comp = ComplaintServices()
        result = comp.get_complaints(total_records=total_records,
                                     page=page,
                                     search=search)
        print(result)
        return jsonify(result)


@app.route('/webapi/complaints/<string:complaint_id>', methods=['GET', 'DELETE'])
@token_required
def delete_complaint(complaint_id):
    if request.method == 'GET':
        """Handle the delete request"""
        # Call the function tho handle the delete
        comp = ComplaintServices()
        result = comp.get_complaint(complaint_id=complaint_id,
                                    user_id=get_user_id())
        return result

    else:
        """Handle the delete request"""
        # Call the function tho handle the delete
        comp = ComplaintServices()
        result = comp.delete_complaint(complaint_id=complaint_id,
                                       user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/standard_messages', methods=['GET', 'POST'])
@token_required
def standard_message(user_id):
    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        message = StandardMessageService()
        result = message.merge_standard_message(smessage=content,
                                                user_id=get_user_id())
        return jsonify(result)

    else:
        """Handle the get request"""
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        msgs = StandardMessageService()
        result = msgs.get_standard_messages(user_id=get_user_id(),
                                            total_records=total_records,
                                            page=page,
                                            search=search)
        return jsonify(result)


@app.route('/webapi/standard_messages/<string:message_id>', methods=['DELETE'])
@token_required
def delete_standard_message(message_id):
    """Handle the delete request"""
    message = StandardMessageService()
    result = message.delete_standard_message(message_id=message_id,
                                             user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/product_copy/<string:ref_id>', methods=['GET'], endpoint="COPY")
@app.route('/webapi/product_edit/<string:ref_id>', methods=['GET'], endpoint="EDIT")
@app.route('/webapi/products', methods=['GET'], endpoint="ALL")
@token_required
def product_unique(ref_id):
    request_endpoint = request.endpoint
    result = ""
    product_service = ProductServices()
    print(request_endpoint)
    if request_endpoint == "ALL":
        print("ok debug1")
        """Handle the get request"""
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        result = product_service.get_products(user_id=get_user_id(),
                                              total_records=total_records,
                                              page=page,
                                              search=search
                                              )

    if request_endpoint == "EDIT":
        result = product_service.get_product(product_id=ref_id,
                                             edit_type="EDIT",
                                             user_id=get_user_id())

    if request_endpoint == "COPY":
        result = product_service.get_product(product_id=ref_id,
                                             edit_type="COPY",
                                             user_id=get_user_id())

    print(result)

    return jsonify(result)


@app.route('/webapi/product_photos/<string:product_id>', methods=['GET'])
@token_required
def product_photos(product_id):
    product_service = ProductServices()
    result = product_service.get_product_photos(product_id=product_id,
                                                user_id=get_user_id())

    print(result)

    return jsonify(result)


@app.route('/webapi/product_colors/<string:product_id>', methods=['GET'])
@token_required
def product_colors(product_id):
    product_service = ProductServices()
    result = product_service.get_product_colors(product_id=product_id,
                                                user_id=get_user_id())

    print(result)

    return jsonify(result)


@app.route('/webapi/product/<string:product_id>', methods=['GET', 'DELETE', 'POST'])
@token_required
def product(product_id):
    product_service = ProductServices()
    if request.method == 'DELETE':
        """Handle the delete request"""
        result = product_service.delete_product(product_id=product_id,
                                                user_id=get_user_id())
        return jsonify(result)

    elif request.method == 'POST':
        content = request.get_json(silent=True)
        result = product_service.post_product(product=content,
                                              user_id=get_user_id())
        return jsonify(result)

    else:
        """Handle the get request"""
        result = product_service.get_product(product_id=product_id,
                                             user_id=get_user_id())
        return jsonify(result)


@app.route('/webapi/product_sold_off', methods=['POST'])
@token_required
def product_sold_off():
    """Handle the get request"""
    content = request.get_json(silent=True)
    product_service = ProductServices()
    result = product_service.post_product_sold_off(product=content,
                                                   user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/product_enable_disable', methods=['POST'])
@token_required
def product_enable_disable():
    """Handle the get request"""
    content = request.get_json(silent=True)
    product_service = ProductServices()
    result = product_service.post_product_enable_disable(product=content,
                                                         user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/products_covers/<string:store_code>', methods=['GET'])
def products_covers(store_code):
    """Handle the get request"""
    start = request.args.get("s", default=0, type=str)
    product_service = ProductServices()
    result = product_service.get_products_covers_front(store_id=get_store_id(store_code=store_code),
                                                       store_code=store_code,
                                                       start=int(start)
                                                       )
    print("debug product id")
    print(result)
    return jsonify(result)


@app.route('/webapi/product_front/<string:product_id>', methods=['GET'])

def product_front(product_id):
    """Handle the get request"""
    product_service = ProductServices()
    result = product_service.get_product_front_one(product_id=product_id)
    return jsonify(result)


@app.route('/webapi/product_photos_front/<string:product_id>', methods=['GET'])
def product_photos_front(product_id):
    """Handle the get request"""
    product_service = ProductServices()
    result = product_service.get_product_photos_front(product_id=product_id)
    return jsonify(result)


@app.route('/webapi/product_colors_front/<string:product_id>', methods=['GET'])
def product_colors_front(product_id):
    """Handle the get request"""
    product_service = ProductServices()
    result = product_service.get_product_colors_front(product_id=product_id)
    return jsonify(result)


@app.route('/webapi/product_colors_front_one/<string:color_id>', methods=['GET'])
def product_colors_front_one(color_id):
    """Handle the get request"""
    product_service = ProductServices()
    result = product_service.get_product_colors_front_one(color_id=color_id)
    return jsonify(result)


@app.route('/webapi/product_categories_front/<string:store_code>/<string:category_name>', methods=['GET'])
def product_categories_front(store_code, category_name):
    """Handle the get request"""
    start = request.args.get("s", default=0, type=str)
    product_service = ProductServices()
    result = product_service.get_product_categories_front(get_store_id(store_code=store_code),
                                                          get_category_id(category_name=category_name),
                                                          store_code=store_code,
                                                          category_name=category_name,
                                                          start=int(start))
    print("debug product front")
    print(result)

    return jsonify(result)


@app.route('/webapi/product_search_front/<string:store_code>/<string:search_word>', methods=['GET'])
def product_search_front(store_code, search_word):
    """Handle the get request"""
    start = request.args.get("s", default=0, type=str)
    product_service = ProductServices()
    result = product_service.get_product_search_front(store_id=get_store_id(store_code=store_code),
                                                      store_code=store_code,
                                                      search_word=search_word,
                                                      start=int(start))
    return jsonify(result)


@app.route('/webapi/product_filters_front/<string:store_code>/<string:search_word>/<string:search_type>/<string:filter_type>',
           methods=['GET'])
def product_filters_front(store_code, search_word, search_type, filter_type):
    """Handle the get request"""
    product_service = ProductServices()
    product_filters = {"result": None}
    if filter_type == "deliver":
        product_filters = product_service.get_product_deliver_filter_front(store_id=get_store_id(store_code=store_code),
                                                                           store_code=store_code,
                                                                           search_word=search_word,
                                                                           search_type=search_type, )

    if filter_type == "public":
        product_filters = product_service.get_product_public_filter_front(store_id=get_store_id(store_code=store_code),
                                                                          store_code=store_code,
                                                                          search_word=search_word,
                                                                          search_type=search_type)

    if filter_type == "price":
        product_filters = product_service.get_product_price_filter_front(store_id=get_store_id(store_code=store_code),
                                                                         store_code=store_code,
                                                                         search_word=search_word,
                                                                         search_type=search_type)

    if filter_type == "state":
        product_filters = product_service.get_product_state_filter_front(store_id=get_store_id(store_code=store_code),
                                                                         store_code=store_code,
                                                                         search_word=search_word,
                                                                         search_type=search_type)

    if filter_type == "CATEGORY":
        product_filters = product_service.get_product_category_filter_front(store_id=get_store_id(store_code=store_code),
                                                                            store_code=store_code,
                                                                            search_word=search_word,
                                                                            search_type=search_type)

    return jsonify(product_filters)


@app.route('/webapi/products_filtered_front/<string:store_code>/<string:search_word>/<string:search_type>', methods=["POST"])
def products_filtered_front(store_code, search_word, search_type):
    """Handle the post request"""
    content = request.get_json(silent=True)

    start = request.args.get("s", default=0, type=str)

    # Call the function tho handle the filtered query
    product_service = ProductServices()

    print(content)
    print(search_word)
    print(search_type)

    result = product_service.get_products_filtered_front(store_id=get_store_id(store_code=store_code),
                                                         store_code=store_code,
                                                         search_word=search_word,
                                                         search_type=search_type,
                                                         json_filter=content,
                                                         start=int(start))

    print(result)

    return jsonify(result)


@app.route('/webapi/favorites', methods=['POST', 'DELETE'])
@token_required
def add_fav_product_front():
    """Handle the POST and DELETE request"""
    favorite_service = FavoritesServices()

    if request.method == "POST":
        content = request.get_json(silent=True)
        result = favorite_service.merge_favorites(favorite=content,
                                                  user_id=get_user_id())
    else:
        favorite_id = request.args.get("fv", default="", type=str)
        result = favorite_service.delete_favorite(favorite_id=favorite_id,
                                                  user_id=get_user_id())

    return jsonify(result)


@app.route('/webapi/fav_products_front/<string:user_id>', methods=['GET'])
@token_required
def fav_products_front(user_id):
    """Handle the get request"""
    favorite_service = FavoritesServices()
    result = favorite_service.get_products_favorites(user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/banners/<string:store_code>', methods=['GET'])
def banners_front(store_code):
    """Handle the get request"""
    banners_service = BannersServices()
    result = banners_service.get_banners_front(store_id=get_store_id(store_code=store_code))
    return jsonify(result)


# TODO VERIFY THE REVIEW IF IT IS NECESSARY TO REQUIRED A TOKEN
@app.route('/webapi/review/<string:ref_id>', methods=['GET', 'DELETE'])
def reviews_front(ref_id):
    if request.method == 'GET':
        """Handle the get request"""
        reviews_service = ReviewServices()
        result = reviews_service.get_reviews_front(ref_id=ref_id)
        return jsonify(result)

    if request.method == 'DELETE':
        """Handle the delete request"""
        review_id = request.args.get("id", default=1, type=str)
        # Call the function tho handle the delete
        rev = ReviewServices()
        result = rev.delete_review(review_id=review_id)
        return jsonify(result)


@app.route('/webapi/reviews/<string:user_id>', methods=['GET', 'PUT'])
@token_required
def reviews(user_id):
    if request.method == 'PUT':
        """Handle the put request"""
        content = request.get_json(silent=True)
        # Call the function tho handle the insert or update
        rev = ReviewServices()
        result = rev.insert_review(review=content,
                                   user_id=get_user_id())
        return jsonify(result)
    else:
        """Handle the get request"""
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        rev = ReviewServices()
        result = rev.get_reviews(user_id=get_user_id(),
                                 total_records=total_records,
                                 page=page,
                                 search=search)
        return jsonify(result)


@app.route('/webapi/cart', methods=['GET'])
@token_required
def get_cart_front(user_id):
    """Handle the get request"""
    cart_service = CartServices()
    result = cart_service.get_user_cart_front(user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/cart', methods=['POST', 'DELETE'])
@token_required
def handle_cart_front():
    """Handle the post and delete request"""
    content = request.get_json(silent=True)

    if request.method == 'POST':
        cart_service = CartServices()
        result = cart_service.post_user_cart_front(product=content,
                                                   user_id=get_user_id())
        return jsonify(result)
    else:

        user_id = content["user_id"]
        store_id = content["store_id"]
        product_id = content["product_id"]
        quantity = content["quantity"]

        if product_id == "None":
            cart_service = CartServices()
            result = cart_service.delete_user_cart_store_front(user_id=get_user_id(),
                                                               store_id=store_id)
        else:
            cart_service = CartServices()
            result = cart_service.delete_user_cart_product_front(user_id=get_user_id(),
                                                                 store_id=store_id,
                                                                 product_id=product_id,
                                                                 quantity=quantity)

        return result


@app.route('/webapi/store_front_one/<string:store_code>', methods=['GET'])
def store_front_one(store_code):
    print("debug store " + store_code)
    """Handle the get request"""
    print("debug 1 - store")
    print("store_code: " + store_code)
    store_service = StoresServices()
    result = store_service.get_store_front_one(store_code=store_code)
    return jsonify(result)


@app.route('/webapi/stores_front', methods=['GET'])
@app.route('/webapi/stores_front/<string:search_word>', methods=['GET'])
def stores_front(search_word="All"):
    """Handle the get request"""
    start = request.args.get("s", default=0, type=str)
    store_service = StoresServices()
    print(search_word)
    result = store_service.get_stores_front(search_word, int(start))
    return jsonify(result)


@app.route('/webapi/fav_stores_front', methods=['GET'])
@token_required
def fav_stores_front():
    """Handle the get request"""
    favorite_service = FavoritesServices()
    result = favorite_service.get_stores_favorites(user_id=get_user_id())
    return jsonify(result)


@app.route('/webapi/messages/<string:customer_profile_id>/<string:store_id>', methods=['GET'])
@token_required
def messages(customer_profile_id, store_id):
    """Handle the get request"""
    message_service = MessageServices()
    result = message_service.get_messages(customer_profile_id=customer_profile_id,
                                          store_id=store_id)
    return jsonify(result)


@app.route('/webapi/message', methods=['POST'])
@token_required
def handle_message_front():
    """Handle the post and delete request"""
    content = request.get_json(silent=True)
    message_service = MessageServices()

    result = message_service.post_message(message=content,
                                          user_id=get_user_id())
    return jsonify(result)

@app.route('/webapi/artists_all_front', methods=['GET'])
@app.route('/webapi/artists_all_front/<string:search_word>', methods=['GET'])
def artists_all_front(search_word="All"):
    """Handle the get request"""
    start = request.args.get("s", default=0, type=str)
    profile_service = ProfileServices()
    result = profile_service.get_artists_all_front(search_word=search_word,
                                                   start=int(start))
    print(result)
    return jsonify(result)


@app.route('/webapi/artists_one_front/<string:profile_id>', methods=['GET'])
def artists_one_front(profile_id):
    """Handle the get request"""
    profile_service = ProfileServices()
    result = profile_service.get_artists_one_front(profile_id=profile_id)
    return jsonify(result)


@app.route('/webapi/artists_profile_products_front/<string:profile_id>', methods=['GET'])
def artists_profile_products_front(profile_id):
    """Handle the get request"""
    product_service = ProductServices()
    result = product_service.get_profile_products_front(profile_id=profile_id)
    return jsonify(result)

#  TODO return all ids to _id

@app.route('/webapi/profile', methods=['POST', 'GET'])
@token_required
def profile_admin():

    if request.method == "GET":
        """Handle the get request"""
        print("debug - ok")
        profile = ProfileServices()
        result = profile.get_profile(user_id=get_user_id())
        if result == "[]":
            return jsonify('[{"_id": {"$oid": "-1"}}]')

    else:
        """Handle the POST request"""
        content = request.get_json(silent=True)
        profile = ProfileServices()
        result = profile.post_profile(profile=content,
                                      user_id=get_user_id())

    return jsonify(result)


@app.route('/webapi/newsletter_contact', methods=['POST'])
@token_required
def handle_newsletter_contact_front():
    """Handle the post request"""
    content = request.get_json(silent=True)
    news_service = NewsletterServices()

    if request.method == 'POST':
        result = news_service.post_newsletter_contact_front(newsletter=content)
        return jsonify(result)

""" CART ACTIONS """
#  TODO verify if the token is necessary on cart too

# 1 Quantity
@app.route('/webapi/cart_item_quantity', methods=['POST'])
def post_cart_item_quantity_front():
    """Handle the post request"""

    content = request.get_json(silent=True)
    cart_service = CartServices()
    result = cart_service.post_cart_product_quantity_front(product=content)
    return jsonify(result)


# 2 Gift
@app.route('/webapi/cart_item_gift', methods=['POST'])
def post_cart_item_gift_front():
    """Handle the post request"""

    content = request.get_json(silent=True)
    cart_service = CartServices()
    result = cart_service.post_cart_product_gift_front(product=content)
    return jsonify(result)


# 3 Observation
@app.route('/webapi/cart_item_observation', methods=['POST'])
def post_cart_item_observation_front():
    """Handle the post request"""

    content = request.get_json(silent=True)
    print(content)
    cart_service = CartServices()
    result = cart_service.post_cart_product_observation_front(product=content)
    return jsonify(result)


# 3 Observation
@app.route('/webapi/cart_coupon', methods=['POST'])
def post_cart_coupon_front():
    """Handle the post request"""

    content = request.get_json(silent=True)
    print(content)
    cart_service = CartServices()
    result = cart_service.post_cart_coupon_front(product=content)
    return jsonify(result)


@app.route('/webapi/contact', methods=['GET', 'POST', 'DELETE', 'PUT'])
@token_required
def contacts():
    if request.method == 'PUT':
        """Handle the put request"""
        content = request.get_json(silent=True)
        # Call the function tho handle the insert or update
        cont = ContactServices()
        result = cont.insert_contact(contact=content)
        return jsonify(result)

    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        # Call the function tho handle the insert or update
        cont = ContactServices()
        result = cont.upsert_contact(contact=content)
        return jsonify(result)

    elif request.method == 'DELETE':
        """Handle the delete request"""
        contact_id = request.args.get("id", default=1, type=str)
        # Call the function tho handle the delete
        cont = ContactServices()
        result = cont.delete_contact(contact_id=contact_id)
        return jsonify(result)

    else:
        """Handle the get request"""
        print("debug apis ")
        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        print(search)
        print(total_records)
        print(page)
        cont = ContactServices()
        result = cont.get_contacts(total_records=total_records,
                                   page=page,
                                   search=search)
        return jsonify(result)


@app.route('/webapi/users', methods=['GET'])
@token_required
def get_users():
    """Handle the get request"""
    print("debug apis ")
    total_records = request.args.get("total_records", default=0, type=int)
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search", default="", type=str)
    user = UsersServices()
    result = user.get_users(total_records=total_records,
                            page=page,
                            search=search)

    return jsonify(result)


@app.route('/webapi/user_enable_disable', methods=['POST'])
@token_required
def user_enable_disable():
    """Handle the get request"""
    content = request.get_json(silent=True)
    user_service = UsersServices()
    result = user_service.post_user_enable_disable(user=content)
    return jsonify(result)


@app.route('/webapi/order/<string:order_id>', methods=['GET', 'DELETE'])
@token_required
def one_order(order_id):
    if request.method == 'DELETE':
        """Handle the delete request"""
        # Call the function tho handle the delete
        order_service = OrdersServices()
        result = order_service.delete_order(order_id=order_id,
                                            user_id=get_user_id()
                                            )
        return jsonify(result)


@app.route('/webapi/order', methods=['POST'])
@token_required
def order_status():
    """Handle the post request"""
    content = request.get_json(silent=True)
    order_service = OrdersServices()
    result = order_service.update_order_status(order=content)
    return jsonify(result)


@app.route('/webapi/orders', methods=['POST', 'GET'])
@token_required
def orders():
    request_endpoint = request.endpoint
    print(request_endpoint)

    if request.method == 'POST':
        """Handle the post request"""
        content = request.get_json(silent=True)
        order_service = OrdersServices()
        result = order_service.merge_order(order=content,
                                           user_id=get_user_id())
        return jsonify(result)


    # TODO verify ths post get
    elif request_endpoint == 'POST_GET':
        content = request.get_json(silent=True)
        total_records = int(content["total_records"])
        page = int(content["page"])
        search = content["search"]
        json_filter = content["checks"]
        order_service = OrdersServices()
        result = order_service.get_orders(user_id=get_user_id(),
                                          total_records=total_records,
                                          page=page,
                                          search=search,
                                          json_filter=json_filter)
        return jsonify(result)

    else:
        """Handle the get request"""
        print("ok get")

        total_records = request.args.get("total_records", default=0, type=int)
        page = request.args.get("page", default=1, type=int)
        search = request.args.get("search", default="", type=str)
        order_service = OrdersServices()
        result = order_service.get_orders(user_id=get_user_id(),
                                          total_records=total_records,
                                          page=page,
                                          search=search,
                                          json_filter="ALL")
        return jsonify(result)


@app.route('/webapi/order_items/<string:order_id>', methods=['GET'])
@token_required
def order_items(order_id):

    order_service = OrdersServices()
    result = order_service.get_order_items(order_id=order_id,
                                           user_id=get_user_id())

    return jsonify(result)


@app.route('/webapi/user_orders', methods=['GET'])
@token_required
def user_orders():

    print("ok user orders")
    total_records = request.args.get("total_records", default=0, type=int)
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search", default="", type=str)
    nmessage = request.args.get("nmessages", default="", type=str)

    order_service = OrdersServices()
    result = order_service.get_user_orders(user_id=get_user_id(),
                                           total_records=total_records,
                                           page=page,
                                           search=search,
                                           nmessages=nmessage)
    return jsonify(result)


@app.route('/webapi/user_store', methods=['GET', 'POST'])
@token_required
def user_store():

    if request.method == 'POST':
        content = request.get_json(silent=True)
        store_service = StoresServices()
        result = store_service.upsert_user_store(content=content,
                                                 user_id=get_user_id())

    else:
        store_service = StoresServices()
        result = store_service.get_user_store(user_id=get_user_id())

    return jsonify(result)


@app.route('/webapi/authenticate_user', methods=['POST'])
def authenticate_user():

    content = request.get_json(silent=True)
    user_service = UsersServices()
    result = user_service.authenticate_user(user=content)
    return jsonify(result)


@app.route('/webapi/create_user_account', methods=['POST'])
def create_user_account():

    content = request.get_json(silent=True)
    user_service = UsersServices()
    result = user_service.create_user_account(user=content)

    return jsonify(result)


@app.route('/webapi/add_message_session', methods=["POST"])
@token_required
def add_message_user_session():
    print("debug 1 session")
    content = request.get_json(silent=True)
    print(content)
    message_service = MessageServices()
    result = message_service.merge_messages_session(message_session=content)

    return jsonify(result)


@app.route('/webapi/message', methods=["POST"])
@token_required
def user_message():
    print("debug 2 session")
    content = request.get_json(silent=True)
    print(content)
    message_service = MessageServices()
    result = message_service.post_message(message=content,
                                          user_id=get_user_id())

    return jsonify(result)


@app.route('/webapi/message_user_session/<string:contact_id>', methods=["GET"])
@token_required
def message_user_session(contact_id):

    message_service = MessageServices()
    result = message_service.get_messages_user_session(contact_id=contact_id)

    return jsonify(result)


if __name__ == '__main__':
    print("try run")
    app.run()
