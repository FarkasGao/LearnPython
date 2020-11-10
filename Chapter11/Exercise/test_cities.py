import unittest
from city_functions import city_country
from city_functions2 import city_country_population

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('tian jin', 'china')
        self.assertEqual(formatted, 'Tian Jin, China')
    def test_city_country_population(self):
        formatted = city_country_population('tian jin', 'china', '1500w')
        self.assertEqual(formatted, 'Tian Jin, China - population 1500w')
        
if __name__ == "__main__":
    unittest.main()