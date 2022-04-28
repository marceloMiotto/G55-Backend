from unittest import TestCase
from service.vacation_notice_service import VacationNoticeServices
from constants import C_SUCCESS


class TestVacationNoticeService(TestCase):
    def test_merge_vacation_message(self):
        vacation_notice = {"vacation_message": "test", "date_range": "", "vacation_receive_message": ""}
        vacation = VacationNoticeServices()
        result = vacation.merge_vacation_message(vacation_notice=vacation_notice,
                                                 user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_get_vacation_message_obj(self):
        vacation = VacationNoticeServices()
        result = vacation.get_vacation_message(store_id="",
                                               user_id="5cec47f4aee7b827eca192c3")
        print(vacation)
        for r in result:
            print(r)
        self.assertEqual(result, result)
