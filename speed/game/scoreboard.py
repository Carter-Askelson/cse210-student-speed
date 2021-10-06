

class Scoreboard:
    """Points earned. The responsibility of Scoreboaard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes:
        score (Scoreboard): The current score.
        
    """

    def __init__(self):
        
        self.score = 0

    def update_score(self):
        self.score += 1
        pass

    def return_score(self):
        self.update_score()
        return self.score

