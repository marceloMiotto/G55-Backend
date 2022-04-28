from database.database_service.database_profile_service import DatabaseProfileService
from service.image_service import ImageService
from constants import C_FRONT_ABSOLUTE_PATH, C_WRK_IMAGE, C_FILE_SEPARATOR, C_IMAGE_SEPARATOR, C_IMG_EXTENSION, \
    C_TEMP_DIR, C_ADMIN_ABSOLUTE_PATH, C_SIZE_670_650, C_LOG_MESSAGE, C_HANDLE_ERROR, C_SUCCESS
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
from service.utils_service import error_to_json, success_to_json
from service.log_service import log


class ProfileServices(object):

    def __init__(self):
        pass

    def get_artists_one_front(self, profile_id):
        try:
            profile = DatabaseProfileService()
            result = profile.get_database_artists_one_front(profile_id=profile_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_artists_one_front", "Handling", str(e), profile_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_artists_all_front(self, search_word, start):
        arguments = ""
        try:
            arguments = "search_word: " + search_word + " - start: " + str(start)
            profile = DatabaseProfileService()
            result = profile.get_database_artists_all_front(search_word=search_word,
                                                            start=start)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("get_artists_all_front", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def handle_profile_photo(self, profile_photo_json):
        """ This function will hanlde the profile photo """
        try:
            self.save_profile_photo(profile_photo_json['src'],
                                    profile_photo_json['store_name'],
                                    profile_photo_json['photo_name'])

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_profile", "Handling", str(e), profile_photo_json))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def post_profile(self, profile, user_id):

        try:
            profile_service = DatabaseProfileService()
            result = profile_service.merge_database_profile(profile=profile,
                                                            user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_profile", "Handling", str(e), profile))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def get_profile(self, user_id):
        """ This function must get all values for profile """
        try:
            profile_service = DatabaseProfileService()
            result = profile_service.get_database_profile(user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("post_profile", "Handling", str(e), "Get profile"))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def delete_profile(self, profile_id, user_id):
        """ The deletion will be in cascade
        """
        try:
            profile_service = DatabaseProfileService()
            result = profile_service.delete_database_profile(profile_id=profile_id,
                                                             user_id=user_id)
            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            log(C_LOG_MESSAGE.format("delete_profile", "Handling", str(e), profile_id))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)

    def save_profile_photo(self, image, profile_id, file_name):
        arguments = ""
        try:
            arguments = "image: " + image + " - store_id: " + profile_id + " - file_name: " + file_name
            # decode the image and create a temporary work item
            image_service = ImageService()
            image = image[23:].encode(encoding="utf-8")
            image_service.decode_img(C_FRONT_ABSOLUTE_PATH, profile_id, image)

            # resize the image for Front End
            img_wrk = image_service.open_image(C_FRONT_ABSOLUTE_PATH + profile_id + C_FILE_SEPARATOR + C_TEMP_DIR +
                                               C_FILE_SEPARATOR + C_WRK_IMAGE + C_IMAGE_SEPARATOR + C_IMG_EXTENSION)

            photo_sizes = C_SIZE_670_650

            img_resized = image_service.resize_img(img=img_wrk, sizes=photo_sizes)
            image_service.save_image(absolute_path=C_FRONT_ABSOLUTE_PATH,
                                     file_id=profile_id,
                                     path='artist/',
                                     file_name=file_name,
                                     image=img_resized)

            image_service.save_image(absolute_path=C_ADMIN_ABSOLUTE_PATH,
                                     file_id=profile_id,
                                     path='artist/',
                                     file_name=file_name,
                                     image=img_resized)

            return success_to_json(str(-1))

        except Exception as e:
            # TODO verify those exceptions
            log(C_LOG_MESSAGE.format("delete_profile", "Handling", str(e), arguments))
            return dumps(error_to_json(C_HANDLE_ERROR.format(str(e))), json_options=RELAXED_JSON_OPTIONS)
