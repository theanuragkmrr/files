from question_model import Question
import html
class QuizBarin:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def next_question(self):
        self.current_question=self.question_list[self.question_number]
        self.question_number+=1
        q_text=html.unescape(self.current_question.text)

        return f"Q.{self.question_number} :{q_text} (True/False): "
        # ans=input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        # self.check_ans(ans,current_question.ans)

    def still_question(self):
        if len(self.question_list)>self.question_number:
            return True
        else:
            return False

    def check_ans(self,ans):
        correct_ans=self.current_question.ans
        if ans.lower()==correct_ans.lower():
            self.score+=1
            return True
        else:
            return False



