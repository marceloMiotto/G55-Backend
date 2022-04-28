from unittest import TestCase
from database.database_service.database_profile_service import DatabaseProfileService
from bson import ObjectId
import datetime


class TestDatabaseProfile(TestCase):

    def test_get_database_artists_one_front(self):
        profile = DatabaseProfileService()
        result = profile.get_database_artists_one_front(profile_id='5d44892875ebfd0bfcc4a697')
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_artists_all_front(self):
        profile = DatabaseProfileService()
        result = profile.get_database_artists_all_front(search_word="All", start=1)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_get_database_profile(self):
        """This function must test the product and product photos"""
        profile = DatabaseProfileService()
        result = profile.get_database_profile(user_id="5d44892875ebfd0bfcc4a697")
        print(result)
        for r in result:
            print(r)
        self.assertEqual(result, result)

    def test_merge_database_profile(self):
        # json object
        profile = {"id": ObjectId("5ced6eaaaee7b843e8d1d209"),
                   "name": "testar",
                   "last_name": "testar",
                   "cpf": 123456789,
                   "cnpj": 12345564,
                   "cell": 1234567,
                   "birthday": "06/03",
                   "history": "test test test test",
                   "photo": 1,
                   "creation_date": str(datetime.datetime.now()),
                   "last_updated_date": str(datetime.datetime.now()),
                   "addresses": [{"cep": 123456789,
                                  "address": "Rua teste 123456",
                                  "number": "5A",
                                  "info": "test",
                                  "reference": "testar",
                                  "neighborhood": "testar",
                                  "state": "RSs",
                                  "city": "Citys",
                                  "type": "",
                                  "identifier": "CONTACsT",
                                  "ship_name": ""
                                  },
                                 {"cep": 123456789,
                                  "address": "Rua teste 123",
                                  "number": "5As",
                                  "info": "teste",
                                  "reference": "test",
                                  "neighborhood": "test",
                                  "state": "RS",
                                  "city": "City",
                                  "type": "",
                                  "identifier": "CONTACTs",
                                  "ship_name": ""
                                  }
                                 ],
                   "ship_address": {"cep": 123456789,
                                  "address": "Rua teste 123456",
                                  "number": "5A",
                                  "info": "test",
                                  "reference": "testar",
                                  "neighborhood": "testar",
                                  "state": "RSs",
                                  "city": "Citys",
                                  "type": "",
                                  "identifier": "CONTACsT",
                                  "ship_name": ""
                                  },
                   "bill_address": {"cep": 123456789,
                                  "address": "Rua teste 123456",
                                  "number": "5A",
                                  "info": "test",
                                  "reference": "testar",
                                  "neighborhood": "testar",
                                  "state": "RSs",
                                  "city": "Citys",
                                  "type": "",
                                  "identifier": "CONTACsT",
                                  "ship_name": ""
                                  },
                   "flag_use_bill_address":"Y"

                   }

        user_id = "5d44892875ebfd0bfcc4a698"
        profile_service = DatabaseProfileService()
        result = profile_service.merge_database_profile(profile=profile,
                                                        user_id=user_id)
        print(result)
        self.assertEqual(result, result)

    def test_delete_database_profile(self):
        profile = DatabaseProfileService()
        result = profile.delete_database_profile(profile_id="5dd8128faee7b8a6dcc0ea2a",
                                                 user_id="5d44892875ebfd0bfcc4a698")
        print(result)
        self.assertEqual(result, result)
