class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        """Navigates to the next question"""
        print(f'[{self.question_number+1}]. {self.question_list[self.question_number].text}')
        userAnswer = input('True or False?   >> ').capitalize()
        self.check_answer(userAnswer)
        self.question_number +=1

    def still_has_questions(self):
        """Determines if there are more questions in the question list left."""
        if len(self.question_list) < self.question_number+1:
            print('[!] You have finished the quiz!' \
            f'Your final score is:   {self.score}/{len(self.question_list)}')
            return False
        return True

    def check_answer(self, answer):
        """Checks if answer is correct or not and adds to the score."""
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            print('[!] You are correct!')
            self.print_score()
        else:
            print('[X] Your answer is wrong. :-(')
            self.print_score()

    def print_score(self):
        """Prints current score statement"""
        print(f'>> Your current score is: {self.score}/{self.question_number+1}\n\n')