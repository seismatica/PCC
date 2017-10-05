import unittest
from city_functions import print_city_country


class TestCaseCityCountry(unittest.TestCase):
    """Test function city_country from city_functions module"""

    def test_city_country_pair(self):
        """Test for names like Santiago, Chile without population input"""
        formatted_city_country = print_city_country("Santiago", "Chile")
        self.assertEqual(formatted_city_country, "Santiago, Chile")

    def test_city_country_population(self):
        """Test for names like Ho Chi Minh City, Vietnam, 8400000"""
        formatted_city_country_population = print_city_country("Santiago", "Chile", 8400000)
        self.assertEqual(formatted_city_country_population, "Santiago, Chile - population 8400000")


unittest.main()
