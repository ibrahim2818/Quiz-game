from question_model import Question
from data import question_data
from quiz_brain import QuesBrain

question_bank=[]
for question in question_data:
     ques= question['text']
     ans= question['answer']
     new_questions= Question(ques, ans)
     question_bank.append(new_questions)

quiz= QuesBrain(question_bank)
while quiz.still_have_question():
     quiz.next_question()
print('you completed the quiz')
print(f"your score is {quiz.score}/{quiz.question_number}")
