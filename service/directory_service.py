from pathlib import Path
from constants import C_FRONT_ABSOLUTE_PATH, C_DUMMY_FILE, C_ADMIN_ABSOLUTE_PATH


class DirectoryService(object):

    def __init__(self):
        pass

    def create_directories(self, store_id):
        self.create_front_store_directories(front_absolute_path=C_FRONT_ABSOLUTE_PATH,
                                            store_id=store_id,
                                            dummy_file=C_DUMMY_FILE)
        self.create_admin_store_directories(admin_absolute_path=C_ADMIN_ABSOLUTE_PATH,
                                            store_id=store_id,
                                            dummy_file=C_DUMMY_FILE)

    def create_directory(self, directory_path):
        path = Path(directory_path)
        path.parent.mkdir(parents=True, exist_ok=True)

    def create_front_store_directories(self, front_absolute_path, store_id, dummy_file):
        store_dir = {store_id: ["banner",
                                "bread_bg",
                                "logo",
                                "profile",
                                "temp",
                                {"product": ["270_270",
                                             "600_600",
                                             "370_370",
                                             "440_440",
                                             "120_140",
                                             "1320_1320",
                                             "thumb"]
                                }]
                    }

        for key, value in store_dir.items():
            self.create_directory(front_absolute_path + key + dummy_file)
            for r in value:

                if "product" in r:
                    for ckey, cvalue in r.items():
                        self.create_directory(front_absolute_path + key + '/' + ckey + dummy_file)
                        for d in cvalue:
                            self.create_directory(front_absolute_path + key + '/' + ckey + '/' + d + dummy_file)

                else:
                    self.create_directory(front_absolute_path + key + '/' + r + dummy_file)

    def create_admin_store_directories(self, admin_absolute_path, store_id, dummy_file):
        store_dir = {store_id: ["banner",
                                "bread_bg",
                                "logo",
                                "profile",
                                "temp",
                                {"product": ["270_270",
                                             "thumb"
                                             ]
                                }]
                    }

        for key, value in store_dir.items():
            self.create_directory(admin_absolute_path + key + dummy_file)
            for r in value:

                if "product" in r:
                    for ckey, cvalue in r.items():
                        self.create_directory(admin_absolute_path + key + '/' + ckey + dummy_file)
                        for d in cvalue:
                            self.create_directory(admin_absolute_path + key + '/' + ckey + '/' + d + dummy_file)

                else:
                    self.create_directory(admin_absolute_path + key + '/' + r + dummy_file)


if __name__ == '__main__':
    pass
