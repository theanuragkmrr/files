from question_model import Question
from data import question_data
from quiz_brain import QuizBarin
from ui import QuizInterface

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_ans=question["correct_answer"]
    new_question=Question(text=question_text,answer=question_ans)
    question_bank.append(new_question)

quiz=QuizBarin(question_bank)
ui=QuizInterface(quiz)
# while quiz.still_question():
#     quiz.next_question()