import unittest
from name_function import get_formatted_name, get_formatted_name2, get_formatted_name3

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_name2(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name2 = get_formatted_name2('janis', 'joplin')
        self.assertEqual(formatted_name2, 'Janis Joplin')
    
    def test_first_last_name3(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name3 = get_formatted_name3('janis', 'joplin')
        self.assertEqual(formatted_name3, 'Janis Joplin')
    
    def test_first_middle_last_name3(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name3 = get_formatted_name3('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name3, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()