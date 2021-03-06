import unittest
from country_codes import get_country_code


class TestGetCountryCode(unittest.TestCase):
    """
    Test the function get_country_code from country_codes module
    """

    def test_output_code(self):
        """
        Test if the function returns the correct country code for a given country
        :return: Comparison between expected country code and country code generated by tested function
        """
        countries = ['Andorra', 'United Arab Emirates', 'Afghanistan']
        expected_answers = {'Andorra': 'ad', 'United Arab Emirates': 'ae', 'Afghanistan': 'af'}

        for country in countries:
            print(get_country_code(country), expected_answers[country])
            self.assertEqual(get_country_code(country), expected_answers[country])


