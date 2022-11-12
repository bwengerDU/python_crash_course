# test the function
import unittest
from city_functions import formatted_city_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_city_country_name(self):
        """Do names like 'Johannesburg, South Africa work?"""
        formatted_name = formatted_city_name('johannesburg', 'south africa')
        self.assertEqual(formatted_name, 'Johannesburg, South Africa')
    def test_city_country_population_name(self):
        """Do responses like 'Johannesburg, South Africa ~ population 1 million work?"""
        formatted_name = formatted_city_name('johannesburg', 'south africa', '12 million')
        self.assertEqual(formatted_name, 'Johannesburg, South Africa ~ Population 12 Million')

if __name__ == '__main__':
    unittest.main()

