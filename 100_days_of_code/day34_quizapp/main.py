from question_model import Question
from quiz_brain import QuizBrain
from ui import Ui
import requests
import html


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()["results"]

question_bank = []

for question in response:
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_gui = Ui(quiz)

