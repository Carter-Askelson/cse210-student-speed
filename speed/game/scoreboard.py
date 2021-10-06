
from .display import Display
class Scoreboard:
    """Points earned. The responsibility of Scoreboaard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes:
        score (Scoreboard): The current score.
        
    """

    def __init__(self):
        self.display = Display
        self.score = 0

    def update_score(self): # this is called below lol
        self.score += 1
        self.display.draw_score(self, self.score) 
        pass

    def return_score(self): # this is called in AnswerCheck.check_answer
        self.update_score()
        return self.score

