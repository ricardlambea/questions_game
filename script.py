

import time

class Question():
    """
    Class that defines a question, keeps the user answer, keeps the
    counter updated, and prints out some messages while the game is 
    running.
    """

    def __init__(self, question, ans_type, correct_answer, level, counter):

        self.question = question
        self.ans_type = ans_type
        self.user_answer = None
        self.correct_answer = correct_answer
        self.level = level
        self._counter = int(counter)

        # Print question
        self.make_question()

        # Get answer from user input
        self.user_answer = self.get_answer()
        
        # Give the right format to answer
        self.process_answer()

        # Print out whether answer is correct or not
        self._points = self.is_correct(self.level)

        # Print a message of the won points
        self.print_won_points(self._points)
        
        # Add the won points to the counter
        self.sum_to_counter()

        # Print the updated counter
        self.print_counter()

    def make_question(self):
        """Print the question on stdout"""
        print(self.question)

    def get_answer(self):
        """Returns the user's answer"""
        return input()
    
    def process_answer(self):
        """Transform the user's answer into the right format"""
        if self.ans_type == "int":
            self.user_answer = int(self.user_answer)
        elif self.ans_type == "str":
            self.user_answer = str(self.user_answer).lower()
        elif self.ans_type == "float":
            self.user_answer = round(float(self.user_answer), 2)
        else:
            raise ValueError("This answer type is not implemented yet.")

    def is_correct(self, level):
        """Check if the answer is correct, and return the corresponding value"""
        if self.user_answer == self.correct_answer:
            return self.q_level(level)
        else:
            return 0
        
    def print_won_points(self, points):
        """
        Print on stdout a customized message depending on whether the answer 
        was correct or not
        """ 
        if points > 0:
            print("Yay! Correct answer!")
            print(f"You get {points} points!")
            print()
        else:
            print("Ooooh... Wrong answer")
            print("You do not get any points")
            print()

    def q_level(self, level):
        """Return a value depending on the question's difficulty"""
        if level == 'easy':
            return 5
        elif level == 'mid':
            return 10
        elif level == 'hard':
            return 15
        
    @property
    def points(self):
        """Return the points won in the current question"""
        return self._points
    
    def print_counter(self):
        """Print the counter value on stdout"""
        print(f"Right now your counter has {self.get_counter} points.") 
        print()

    @property
    def get_counter(self):
        """Return the value of the current counter"""
        return self._counter

    def sum_to_counter(self):
        """
        Sum the points won in the current question to the points that were 
        already on the counter
        """
        self._counter = self._counter + self.points


if __name__=='__main__':

    print(
        "This is The HaGE (Hardest Game Ever). A trivial-like mini-game in which \n" +
        "you have to answer some questions, and for each question, and difficulty, \n" +
        "you will get different points. Try to gain as many points as you can. \n" +
        "Good luck!!!\n\n"
    )
    # Suported types of questions: 'str', 'int', 'float'
    # You start with a 0 on your counter 
    q1 = Question("Which is the root square of 452?", "float", "21.26", "hard", 0)
    q2 = Question("Write the number 4 in binary", "str", "100", "mid", q1.get_counter)
    q3 = Question("How many planets are there in the solar system?", "int", "8", "easy", q2.get_counter)

    print(f"The game has finished. You got a total of {q3.get_counter} points. Congrats!")


