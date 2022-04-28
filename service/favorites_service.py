from database.database_service.database_favorites_service import DatabaseFavoritesService
from service.image_service import ImageService
from constants import C_FRONT_ABSOLUTE_PATH, C_WRK_IMAGE, C_FILE_SEPARATOR, C_IMAGE_SEPARATOR, C_IMG_EXTENSION, \
    C_TEMP_DIR, C_SIZE_120_140, C_SIZE_270_270, C_SIZE_370_370, C_SIZE_440_440, C_SIZE_600_600, C_SIZE_1320_1320, \
    C_ADMIN_ABSOLUTE_PATH, C_SIZE_THUMB, C_HANDLE_ERROR, C_LOG_MESSAGE
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, ObjectId, loads
from service.log_service import log
from service.utils_service import error_to_json
from service.page_pagination_service import PagePaginationService


class FavoritesServices(object):

    def __init__(self):
        pass

    def merge_favorites(self, favorite, user_id):
        try:
            fav_service = DatabaseFavoritesService()
            result = fav_service.merge_database_favorites(favorite=favorite,
                                                          user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("merge_favorites", "Handling", str(e), favorite))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_favorite(self, favorite_id, user_id):
        try:
            fav_service = DatabaseFavoritesService()
            result = fav_service.delete_database_favorite(favorite_id=favorite_id,
                                                          user_id=user_id)
            return result

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_favorite", "Handling", str(e), str(favorite_id)))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_products_favorites(self, user_id):
        try:
            fav_service = DatabaseFavoritesService()
            result = fav_service.get_database_favorite_products(user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_products_favorites", "Handling", str(e), str(user_id)))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_stores_favorites(self, user_id):
        try:
            fav_service = DatabaseFavoritesService()
            result = fav_service.get_database_favorite_stores(user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_stores_favorites", "Handling", str(e), str(user_id)))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)