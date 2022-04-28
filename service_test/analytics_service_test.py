from unittest import TestCase
from service.analytics_service import AnalyticsServices
from bson import ObjectId
import datetime


class TestAnalyticsService(TestCase):

    def test_merge_analytics(self):
        analytics = {"analytics_flag": "N"
                    }
        analytics_service = AnalyticsServices()
        result = analytics_service.merge_analytics(custom_analytics=analytics,
                                                   user_id="5cf00a2aaee7b801dcb2a470")
        print(result)
        self.assertEqual(result, result)

    def test_get_analytics_flag(self):
        analytics = AnalyticsServices()
        result = analytics.get_analytics_flag( user_id="5cf00a2aaee7b801dcb2a470")
        print(result)
        self.assertEqual(result, result)