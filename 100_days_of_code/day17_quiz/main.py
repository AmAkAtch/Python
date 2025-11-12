from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain 

question_bank = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = QuestionModel(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.has_next_question():
    print(quiz.next_question())