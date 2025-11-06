class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        return True


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q{self.question_number}: {question.question} (True/False)")
        c_answer = question.answer
        self.check_answer(u_answer,c_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")

            self.score += 1

        else:
            print(f"You got it wrong :(, the real answer was {c_answer}")

        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")


