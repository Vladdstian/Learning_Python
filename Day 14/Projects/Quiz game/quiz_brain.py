class QuizBrain:
    
    def __init__(self, list):
        self.question_number = O
        self.question_list = list 

    def next_question(self):
        question = self.question_list[self.question_number] 
        text = f"Q{self.question_number + 1} - {question['text']}"
        answer = input(text)
        
        
            

    