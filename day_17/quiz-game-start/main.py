from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
import random
from os import system

question_bank = []
quiz = QuizBrain(question_bank)

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

while quiz.still_has_questions():
    quiz.next_question()
