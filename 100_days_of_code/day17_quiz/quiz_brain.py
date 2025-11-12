class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.correct_answer_count = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {question} (True/False)? ").lower()
        
        if user_answer == answer:
            self.correct_answer_count += 1
            print(f"You gave {self.correct_answer_count}/{self.question_number} correct answers!")
        else:
            print(f"You gave {self.correct_answer_count}/{self.question_number} correct answers!")

    def has_next_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Thanks for playing, Your final score is {self.correct_answer_count}/{self.question_number}")
            return False