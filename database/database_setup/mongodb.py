# import mongoengine as me
from mongoengine import connect
# import pymongo
from pymongo import MongoClient
from constants import C_MONGO_DATABASE


def mongodb_conn():
    connect(C_MONGO_DATABASE)


def mongopy_conn():
    client = MongoClient()
    db = client.galeria55
    return db


db_conn = mongopy_conn()


class MongoCollection(object):

    def category_cities(self):
        collection = db_conn.category_cities
        return collection

    def category_states(self):
        collection = db_conn.category_states
        return collection

    def message_contacts(self):
        collection = db_conn.message_contacts
        return collection

    def messages(self):
        collection = db_conn.messages
        return collection

    def reviews(self):
        collection = db_conn.reviews
        return collection

    def user_carts(self):
        collection = db_conn.user_carts
        return collection

    def banners(self):
        collection = db_conn.banners
        return collection

    def categories(self):
        collection = db_conn.categories
        return collection

    def product_colors(self):
        collection = db_conn.product_colors
        return collection

    def product_photos(self):
        collection = db_conn.product_photos
        return collection

    def products(self):
        collection = db_conn.products
        return collection

    def stores(self):
        collection = db_conn.stores
        return collection

    def user_favorites(self):
        collection = db_conn.user_favorites
        return collection

    def users(self):
        collection = db_conn.users
        return collection

    def newsletters(self):
        collection = db_conn.newsletter
        return collection

    def coupons(self):
        collection = db_conn.coupons
        return collection

    def contacts(self):
        collection = db_conn.contacts
        return collection

    def complaints(self):
        collection = db_conn.complaints
        return collection

    def analytics(self):
        collection = db_conn.analytics
        return collection

    def freight_types(self):
        collection = db_conn.freight_types
        return collection

    def profiles(self):
        collection = db_conn.profiles
        return collection

    def standard_messages(self):
        collection = db_conn.standard_messages
        return collection

    def vacation_notices(self):
        collection = db_conn.vacation_notices
        return collection

    def orders(self):
        collection = db_conn.orders
        return collection

    def order_items(self):
        collection = db_conn.order_items
        return collection

    def sessions(self):
        collection = db_conn.sessions
        return collection

    def messages_session(self):
        collection = db_conn.messages_session
        return collection


if __name__ == '__main__':
    print("test execution of file mongodb")
