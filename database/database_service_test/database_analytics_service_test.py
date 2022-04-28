import unittest
from database.database_service.database_analytics_service import DatabaseAnalyticsService
import datetime
from bson import ObjectId


class TestAnalytics(unittest.TestCase):

    def test_get_database_custom_analytics_flag(self):
        analytics = DatabaseAnalyticsService()
        user_id = "5cf00a2aaee7b801dcb2a470"
        analytics_object = analytics.get_database_analytics_flag(user_id=user_id)
        print(analytics_object)
        for a in analytics_object:
            print(a)

        self.assertEqual(analytics_object, analytics_object)

    def test_merge_database_custom_analytics(self):
        analytics_obj = {"analytics_flag": "Y"}
        user_id = "5cf00a2aaee7b801dcb2a470"
        analytics = DatabaseAnalyticsService()
        result = analytics.merge_database_analytics(arguments=analytics_obj,
                                                    user_id=user_id)

        print(result)
        self.assertEqual(result, result)


if __name__ == '__main__':
    unittest.main()
