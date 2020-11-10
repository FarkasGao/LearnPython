import json
from survey import OpenVote #AnonymousSurvey

filename = 'favorite_languages2.json'

# 定义一个问题，并创建一个调查
question = "What language did you first learn to speak?"
my_survey = OpenVote(question, filename)

#显示问题并存储答案

print("Enter 'q' at any time to quit.\n")
while True:
    my_survey.show_question()
    print("Enter 'f' finsh your vote")
    username = input("Enter your name: ")
    if username == 'q':
        break
    response = []
    while True:
        ans = input("Language: ")
        if ans == 'f':
            break
        if ans == 'q':
            break
        response.append(ans)
    if ans == 'q':
        break
        
    my_survey.store_response(username, response)

        
#显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

#print("statistical result:")
#my_survey.read_results()
#my_survey.show_different_results()