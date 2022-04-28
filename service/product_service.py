from database.database_service.database_product_service import DatabaseProductService
from service.image_service import ImageService
from constants import C_FRONT_ABSOLUTE_PATH, C_WRK_IMAGE, C_FILE_SEPARATOR, C_IMAGE_SEPARATOR, C_IMG_EXTENSION, \
    C_TEMP_DIR, C_SIZE_120_140, C_SIZE_270_270, C_SIZE_370_370, C_SIZE_440_440, C_SIZE_600_600, C_SIZE_1320_1320, \
    C_ADMIN_ABSOLUTE_PATH, C_SIZE_THUMB, C_HANDLE_ERROR, C_LOG_MESSAGE
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, ObjectId, loads
from service.log_service import log
from service.utils_service import error_to_json
from service.page_pagination_service import PagePaginationService


class ProductServices(object):

    def __init__(self):
        pass

    def get_profile_products_front(self, profile_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_profile_products_front(profile_id=profile_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_profile_products_front", "Handling", str(e), profile_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_products_covers_front(self, store_id, store_code, start):
        arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + " - start: " + str(start)
        try:
            products = DatabaseProductService()
            result = products.get_database_products_front(store_id=store_id,
                                                          store_code=store_code,
                                                          start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_products_covers_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_front_one(self, product_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_front_one(product_id=product_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_front_one", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_photos_front(self, product_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_photos_front(product_id=product_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_photos_front", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_colors_front(self, product_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_colors_front(product_id=product_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_colors_front", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_colors_front_one(self, color_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_colors_front_one(color_id=color_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_colors_front_one", "Handling", str(e), color_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_categories_front(self, store_id, category_id, store_code, category_name, start):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + "category_id: " + str(category_id) + \
                        " - store_code: " + store_code + \
                        " - category_name: " + category_name + " - start: " + str(start)
            products = DatabaseProductService()
            result = products.get_database_product_categories_front(store_id=store_id,
                                                                    category_id=category_id,
                                                                    store_code=store_code,
                                                                    category_name=category_name,
                                                                    start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_categories_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_search_front(self, store_id, store_code, search_word, start):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - start: " + str(start)
            products = DatabaseProductService()
            result = products.get_database_product_search_front(store_id=store_id,
                                                                store_code=store_code,
                                                                search_word=search_word,
                                                                start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_search_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_public_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            products = DatabaseProductService()
            result = products.get_database_product_public_filter_front(store_id=store_id,
                                                                       store_code=store_code,
                                                                       search_word=search_word,
                                                                       search_type=search_type)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_public_filter_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_price_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            products = DatabaseProductService()
            result = products.get_database_product_price_filter_front(store_id=store_id,
                                                                      store_code=store_code,
                                                                      search_word=search_word,
                                                                      search_type=search_type)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_price_filter_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_deliver_filter_front(self, store_id, store_code, search_word, search_type):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            products = DatabaseProductService()
            result = products.get_database_product_deliver_filter_front(store_id=store_id,
                                                                        store_code=store_code,
                                                                        search_word=search_word,
                                                                        search_type=search_type)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_deliver_filter_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_state_filter_front(self, store_id, store_code, search_word, search_type):
        try:
            arguments = "store_id: " + str(store_id) + " - store_code" + store_code +\
                        " - search_word: " + search_word + " - search_type: " + search_type
            products = DatabaseProductService()
            result = products.get_database_product_state_filter_front(store_id=store_id,
                                                                      store_code=store_code,
                                                                      search_word=search_word,
                                                                      search_type=search_type)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_state_filter_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_category_filter_front(self, store_id, store_code, search_word, search_type):
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type
            products = DatabaseProductService()
            result = products.get_database_product_category_filter_front(store_id=store_id,
                                                                         store_code=store_code,
                                                                         search_word=search_word,
                                                                         search_type=search_type)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_category_filter_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_products_filtered_front(self, store_id, store_code, search_word, search_type, json_filter, start):
        arguments = ""
        try:
            arguments = "store_id: " + str(store_id) + " - store_code: " + store_code + \
                        " - search_word: " + search_word + " - search_type: " + search_type + \
                        " - json_filter: " + str(json_filter) + " - start: " + str(start)
            products = DatabaseProductService()
            result = products.get_database_products_filtered_front(store_id=store_id,
                                                                   store_code=store_code,
                                                                   search_word=search_word,
                                                                   search_type=search_type,
                                                                   json_filter=json_filter,
                                                                   start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_products_filtered_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_product(self, product, user_id):
        try:
            photos = []
            color_photos = []
            colors = []
            color_sizes = []
            product_service = DatabaseProductService()
            result = product_service.merge_database_product(product)
            r = loads(result)
            product_id = r["id"]
            print(product_id)

            if product["color_flag"] == "N":
                print(product)
                product_photos = {"product_id": product_id}
                for p in product["photos"]:
                    for obj in p:
                        print(obj)
                        #  save the photos
                        self.save_product_photos(image=p[obj]["src"],
                                                 store_id=product["store_id"],
                                                 file_name=p[obj]["name"])
                        photos.append({"name": p[obj]["name"],
                                       "order": p[obj]["order"],
                                       "src": p[obj]["src"]})

                product_photos["photos"] = photos
                result_photos = product_service.merge_database_product_photos(product_photos=product_photos,
                                                                              user_id=user_id)
                #   TODO PERFORM THE EXCEPTION CASE
            else:
                for p in product["colors"]:
                    print(p)
                    for key in p:
                        print(p[key])
                        product_colors = {"product_id": product_id,
                                          "color_name": p[key]["name"]}
                        for photos in p[key]["photos"]:
                            for pkey in photos:
                                self.save_product_photos(image=photos[pkey]["src"],
                                                         store_id=product["store_id"],
                                                         file_name=photos[pkey]["photo_name"])
                                color_photos.append({"name": photos[pkey]["photo_name"],
                                                     "order": photos[pkey]["order"],
                                                     "src": photos[pkey]["src"]})

                        for sizes in p[key]["sizes"]:
                            print(sizes)
                            for skey in sizes:
                                color_sizes.append({"size": sizes[skey]["size"],
                                                    "quantity": sizes[skey]["stock_quantity"]})

                        print(product_colors)
                        product_colors["photos"] = color_photos
                        product_colors["sizes"] = color_sizes
                        result_colors = product_service.merge_database_product_colors(product_colors=product_colors)
                        print(result_colors)
                        #   TODO PERFORM THE EXCEPTION CASE
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_product", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product(self, product_id, user_id):
        arguments = ""
        try:
            arguments = "product_id: " + product_id
            product_service = DatabaseProductService()
            result = product_service.get_database_product(product_id=product_id,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_photos(self, product_id, user_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_photos(product_id=product_id,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_photos", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_product_colors(self, product_id, user_id):
        try:
            products = DatabaseProductService()
            result = products.get_database_product_colors(product_id=product_id,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)
        except Exception as e:
            log(C_LOG_MESSAGE.format("get_product_colors", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_products_count(self, user_id, search):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " search: " + search
            comps = DatabaseProductService()
            result = comps.get_database_products_count(user_id=user_id, search_word=search)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_products_count", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_products(self, user_id, total_records, page, search):
        arguments = ""
        try:
            arguments = "user_id: " + user_id + " total_records: " + str(total_records) + \
                        " - page: " + str(page) + " - search: " + search

            comps = DatabaseProductService()
            if total_records == 0:
                total_records = self.get_products_count(user_id=user_id, search=search)

            pagination_service = PagePaginationService(total_records=total_records, page=page)

            if total_records == 0:
                result_header = pagination_service.serialize
                return result_header

            stop_limit = pagination_service.get_higher_limit()

            if stop_limit >= total_records:
                stop_limit = total_records

            start_limit = pagination_service.get_lower_limit() - 1

            if start_limit >= stop_limit:
                return None

            result = comps.get_database_products(user_id=user_id,
                                                 search_word=search,
                                                 start=page)

            result_header = pagination_service.serialize
            result_header["rows"] = dumps(result, json_options=RELAXED_JSON_OPTIONS)

            return result_header

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_products", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_product(self, product_id, user_id):
        try:
            product = DatabaseProductService()
            result = product.delete_database_product(product_id=product_id,
                                                     user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_product", "Handling", str(e), product_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_product_sold_off(self, product, user_id):
        try:
            product_service = DatabaseProductService()
            result = product_service.post_database_product_sold_off(product=product,
                                                                    user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_product_sold_off", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_product_enable_disable(self, product, user_id):
        try:
            product_service = DatabaseProductService()
            result = product_service.post_database_product_enable_disable(product=product,
                                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_product_enable_disable", "Handling", str(e), product))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def save_product_photos(self, image, store_id, file_name):
        arguments = ""
        try:
            arguments = "image: " + image + " - store_id: " + str(store_id) + \
                        "file_name: " + file_name
            # decode the image and create a temporary work item
            image_service = ImageService()
            image = image[23:].encode(encoding="utf-8")
            image_service.decode_img(C_FRONT_ABSOLUTE_PATH, str(store_id), image)

            # resize the image for Front End
            img_wrk = image_service.open_image(C_FRONT_ABSOLUTE_PATH + str(store_id) + C_FILE_SEPARATOR + C_TEMP_DIR +
                                               C_FILE_SEPARATOR + C_WRK_IMAGE + C_IMAGE_SEPARATOR + C_IMG_EXTENSION)

            product_dir = ["120_140", "270_270", "370_370", "440_440", "600_600", "1320_1320", "thumb"]
            for d in product_dir:

                photo_sizes = (0, 0)
                if d == "120_140":
                    photo_sizes = C_SIZE_120_140
                elif d == "270_270":
                    photo_sizes = C_SIZE_270_270
                elif d == "370_370":
                    photo_sizes = C_SIZE_370_370
                elif d == "440_440":
                    photo_sizes = C_SIZE_440_440
                elif d == "600_600":
                    photo_sizes = C_SIZE_600_600
                elif d == "1320_1320":
                    photo_sizes = C_SIZE_1320_1320
                elif d == "thumb":
                    photo_sizes = C_SIZE_THUMB

                img_resized = image_service.resize_img(img=img_wrk, sizes=photo_sizes)
                if d == "270_270" or d == "thumb":
                    image_service.save_image(absolute_path=C_ADMIN_ABSOLUTE_PATH,
                                             store_id=str(store_id),
                                             path='product/' + d,
                                             file_name=file_name,
                                             image=img_resized)

                image_service.save_image(absolute_path=C_FRONT_ABSOLUTE_PATH,
                                         store_id=str(store_id),
                                         path='product/' + d,
                                         file_name=file_name,
                                         image=img_resized)
        except Exception as e:
            log(C_LOG_MESSAGE.format("save_product_photos", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)


