from PIL import Image
from constants import C_IMG_EXTENSION, C_WRK_IMAGE, C_TEMP_DIR, C_FILE_SEPARATOR, C_IMAGE_SEPARATOR
import base64
import io


class ImageService(object):

    def __init__(self):
        pass

    def save_image(self, absolute_path, file_id, path, file_name, image):
        try:
            image.save(absolute_path + file_id + C_FILE_SEPARATOR + path + C_FILE_SEPARATOR +
                       file_name + C_IMAGE_SEPARATOR + C_IMG_EXTENSION)

        except IOError as e:
            print(str(e))

    def open_image(self, path):
        try:
            img = Image.open(path)
            return img
        except IOError as e:
            print(str(e))

    def create_thumbnail(self, img, sizes):
        try:
            img.thumbnail(sizes)
            return img
        except IOError as e:
            print(str(e))

    def resize_img(self, img, sizes):
        try:
            img = img.resize(sizes)
            return img
        except IOError as e:
            print(str(e))

    def crop_img(self, img):
        try:
            width, height = img.size
            area = (0, 0, width / 2, height / 2)
            img = img.crop(area)
            return img

        except IOError as e:
            print(str(e))

    def decode_img(self, absolute_path, file_id, original_image):
        try:
            with open(absolute_path + file_id + C_FILE_SEPARATOR + C_TEMP_DIR +
                      C_FILE_SEPARATOR + C_WRK_IMAGE + C_IMAGE_SEPARATOR + C_IMG_EXTENSION, "wb") as fh:
                fh.write(base64.decodebytes(original_image))
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    pass


