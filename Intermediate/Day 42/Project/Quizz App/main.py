from question_model import Question
from quiz_brain import QuizBrain
import tkinter as tk
import requests

difficulty = input("What difficulty would you like to play? easy/medium/hard\n")
no_of_questions = int(input("How many questions would you like to answer?\n"))

url_text = f"https://opentdb.com/api.php?amount={no_of_questions}&category=11&difficulty={difficulty}&type=boolean"
print(url_text)
question_data = requests.get(url=url_text).json()["results"]

print(question_data)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
