import json

class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""
    
    def __init__(self, question,filename):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []
        self.count = {}
        self.filename = filename
        
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
        
    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)
        with open(self.filename, 'w') as f:
            json.dump(self.responses, f)
        
    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            for survey in response:
                print(f"- {survey}  ", end='')
            print()
            
    def show_different_results(self):
        """显示收集到的不同结果并计数"""
        sum_languages = []
        for response in self.responses:
            for survey in response:
                sum_languages.append(survey.title())
                
        results = set(sum_languages)
        print(results)
        for result in results:
            number = 0
            for sum_language in sum_languages:
                if result == sum_language:
                    number += 1
            self.count[result] = number
        print(self.count)

    def read_results(self):
        """读取收集到的结果"""
        with open(self.filename) as f:
            self.responses = json.load(f)   

class OpenVote(AnonymousSurvey):
    def __init__(self, question, filename):
        super().__init__(question, filename)
        self.question = question
        self.responses = {}
        self.count = {}
        
    def store_response(self, voter, new_response):
        """存储单份调查问卷"""
        self.responses[voter] = new_response
        with open(self.filename, 'w') as f:
            json.dump(self.responses, f)
           
    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for name, languages in self.responses.items():
            print(name, ":")
            for language in languages:
                print("  -",language,end='')
            print()