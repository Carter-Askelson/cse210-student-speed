import arcade
from .wordbank import WordBank
from .display import Display
from .scoreboard import Scoreboard


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        score (Scoreboard): The current score.
        words (wordbank): 5 words that get sent to display
    """

    def __init__(self):
        self.word_list = []
        self.score = 0
        self.game_score = Scoreboard()
        self.game_screen = Display()
        self.game_word_bank = WordBank()

    def start_game(self):
        self.word_list = self.game_word_bank.get_words()
        print(self.word_list)
        # self.update_screen_score()
        self.game_screen.render_game(0, self.word_list)


    # def update_screen_score(self):
    #     self.game_score.update_score()
    #     self.score = self.game_score.return_score()
