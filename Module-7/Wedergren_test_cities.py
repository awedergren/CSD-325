# Amanda Wedergren
# April 16, 2025
# Module 7.2 Assignment

from city_functions import format_location
import unittest

class CityTestCase(unittest.TestCase):

    def test_city_country(self):

        city_country = format_location('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile - population , ')


if __name__ == '__main__':
    unittest.main()