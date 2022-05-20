from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"] 
    question_bank.append(Question(text=question_text, answer=question_answer))

print(question_bank)

