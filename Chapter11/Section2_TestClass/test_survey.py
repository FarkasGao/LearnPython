import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试。"""
    def test_store_single_response(self):
        """测试单个答案会被妥善的储存"""
        question = "What language did you first learn to speak?"
        filename = "favorite_languages2.json"
        my_survey = AnonymousSurvey(question, filename)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()