import unittest
from city_functions import city_country

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('bei jing', 'china')
        self.assertEqual(formatted, 'Bei Jing, China')
        
if __name__ == '__main__':
    unittest.main()