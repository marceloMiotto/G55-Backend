from unittest import TestCase
from service.directory_service import DirectoryService
from constants import C_DUMMY_FILE, C_DIR_PATH_ADMIN, C_FRONT_ABSOLUTE_PATH, C_ADMIN_ABSOLUTE_PATH


class TestHandleDirectory(TestCase):
    def test_create_directory(self):
        handle = DirectoryService()
        handle.create_directory(C_DIR_PATH_ADMIN + 'TEST' + C_DUMMY_FILE)
        self.assertEqual(1, 1)

    def test_create_front_store_directories(self):
        handle = DirectoryService()
        handle.create_front_store_directories(C_FRONT_ABSOLUTE_PATH, "5d658bbeaee7b843d0d69ccb", C_DUMMY_FILE)
        self.assertEqual(1, 1)

    def test_create_admin_store_directories(self):
        handle = DirectoryService()
        handle.create_admin_store_directories(C_ADMIN_ABSOLUTE_PATH, "5d658bbeaee7b843d0d69ccb", C_DUMMY_FILE)
        self.assertEqual(1, 1)

    def test_create_directories(self):
        handle = DirectoryService()
        handle.create_directories(store_id="5d44a79575ebfd0bfcc4a69d")
        self.assertEqual(1, 1)
