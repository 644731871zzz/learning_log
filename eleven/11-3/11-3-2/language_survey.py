from survey import AnonymousSurvey

#定义一个问题,并显示一个调查的AnoymousSurvey
question="What language did you first learn to speak? "
language_survey=AnonymousSurvey(question)

#显示问题并存储答案
language_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response=input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#显示调查结果
print("\nthank you to everyone who participated in the survey!")
language_survey.show_results()

