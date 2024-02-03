from quiz_files import question_data

class Question:
    def __init__(self, q_text, q_ans):
        self.text = q_text
        self.answer = q_ans

class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/ False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print(f"You got it right!")
            
        else:
            print("You are wrong")
        print(f"The correct answer was: {correct_answer}\nYour current score is {self.user_score}/{self.question_number}\n")

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

my_question = QuizBrain(question_bank)
while my_question.still_has_questions():
    my_question.next_question()
print(f"You'v completed the quiz\nYour final score is {my_question.user_score} / {my_question.question_number}")
