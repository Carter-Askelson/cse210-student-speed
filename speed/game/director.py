import arcade
from game.wordbank import WordBank
from game.display import Display
from game.scoreboard import Scoreboard

class Director():
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
        self.add_words(5)
        self.update_screen_score()
        self.game_screen.start_rendering()
        self.game_screen.render_game(self.score, self.word_list)

        
    

    def add_words(self, number):
        self.word_list = self.game_word_bank.get_words(number)
        self.word_list = self.game_word_bank.update_list()

    def update_screen_score(self):
        self.game_score.update_score()
        self.score = self.game_score.return_score()


