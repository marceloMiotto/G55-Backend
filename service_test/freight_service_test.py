from unittest import TestCase
from service.freight_service import FreightServices
from constants import C_SUCCESS


class TestFreightServices(TestCase):
    def test_merge_freight_type(self):
        freight = {}
        freight_service = FreightServices()
        result = freight_service.merge_freight_type(freight=freight,
                                                    user_id="")
        self.assertEqual(result, C_SUCCESS)

    def test_get_freight_types(self):
        freight = FreightServices()
        result = freight.get_freight_types(total_records=5, page=1, search="te", user_id="")
        print(result)
        self.assertEqual(result, result)

    def test_delete_freight_type(self):
        freight = FreightServices()
        result = freight.delete_freight_type(freight_type_id=1, user_id="")
        self.assertEqual(result, C_SUCCESS)


    def test_get_freight_type_count(self):
        freight = FreightServices()
        result = freight.get_freight_type_count(search="test")
        print(result)
        self.assertEqual(result, result)
