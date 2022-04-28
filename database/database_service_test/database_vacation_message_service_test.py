from unittest import TestCase
from database.database_service.database_vacation_message_service import DatabaseVacationNotice
from bson import ObjectId
import datetime


class TestDatabaseVacationService(TestCase):

    def test_get_vacation_message_obj(self):
        vacation = DatabaseVacationNotice()
        result = vacation.get_database_vacation_message(store_id="5cec47f4aee7b827eca192c3",
                                                        user_id="5d729ddeaee7b89398d77b08")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_vacation_message(self):
        vacation = DatabaseVacationNotice()
        vacation_notice = {"date_range": "2019-05-16 2019-06-15",
                           "vacation_message": "test",
                           "vacation_receive_message": "Y",
                           "creation_date": str(datetime.datetime.now()),
                           "last_updated_date": str(datetime.datetime.now()),
                           "store_id": ObjectId("5cec47f4aee7b827eca192c3")}
        result = vacation.merge_database_vacation_message(vacation_notice=vacation_notice,
                                                          user_id="5d729ddeaee7b89398d77b08")
        print(result)
        self.assertEqual(result, result)

