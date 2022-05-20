from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question_bank.append(Question(text=question_text, answer=question_answer))

# print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
