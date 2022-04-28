from unittest import TestCase
from database.database_service.database_freight_service import DatabaseFreightTypeService
from constants import C_SUCCESS
from bson import ObjectId
import datetime


class TestDatabaseFreightTypeService(TestCase):

    def test_get_freight_types(self):
        freights = DatabaseFreightTypeService()
        result = freights.get_database_freight_types(search_word="te", start=1, user_id="5cf1635faee7b829843cf745")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_delete_freight_types(self):
        freight = DatabaseFreightTypeService()
        freights = freight.delete_database_freight_types(freight_type_id="5dd80ebfaee7b8c724cb93db",
                                                         user_id="5cf1635faee7b829843cf745")
        self.assertEqual(freights, freights)

    def test_merge_freight_type(self):
        freight = DatabaseFreightTypeService()
        freight_json = {"name": "Test2"
                      }
        freights = freight.merge_database_freight_type(freight=freight_json,
                                                       user_id="5cf1635faee7b829843cf745")
        print(freights)
        self.assertEqual(freights, freights)

    def test_get_database_freight_count(self):
        freight = DatabaseFreightTypeService()
        result = freight.get_database_freight_count(search="te")
        print(result)
        self.assertEqual(result, result)
