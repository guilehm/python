import unittest
from exercicio_cidadePais import get_city_country


class NamesTestCase(unittest.TestCase):
    """ Teste para exercicio_cidadePais.py """

    def test_city_country(self):
        city_country = get_city_country('goiania', 'brasil')
        self.assertEqual(city_country, 'Goiania , Brasil')


unittest.main()
