import arcade
from settings import Settings
import random


class Display():
    """Outputs the game state. The responsibility of the class is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        
    """

    def __init__(self):   
        """Sets the screen size, starting point for the words, and the speeds the words bounce across the screen. 
    
        Stereotype: 
            Constructor

        Arguments:
            None
            
        """
        #maybe get these from settings.py?
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        self.SCREEN_TITLE = "Welcome to SPEED"
        self.RADIUS = 150
        self.changing_x0 = random.randint(0,600)
        self.changing_x1 = random.randint(0,600)
        self.changing_x2 = random.randint(0,600)
        self.changing_x3 = random.randint(0,600)
        self.changing_x4 = random.randint(0,600)
        self.changing_d0 = random.randint(300,600)
        self.changing_d1 = random.randint(300,600)
        self.changing_d2 = random.randint(300,600)
        self.changing_d3 = random.randint(300,600)
        self.changing_d4 = random.randint(300,600)
        self.word_list = ["Example Text1", "Example Text2", "Example Text3", "Example Text4", "Example Text5"]
        
        

   
        
    
    

    def render_game(self, new_score = 0, new_wordlist = ["Example Text1", "Example Text2", "Example Text3", "Example Text4", "Example Text5"]):
        """Opens the Window of the Game and make the game render a new screen 80 times a second.
    
        Stereotype: 
            Service Provider

        Arguments:
            new_score (answerchecker)
            new_wordlist (wordbank)
            
        """
        arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        
        arcade.schedule(self.on_draw, 1 / 80)
        #these next 3 probably need to go to on_draw
        #display score
        #display each word in word_list, needs to change a word everytime the player guesses one
        #display buffer
        
        arcade.run()

    def on_draw(self, delta_time):

        """Displays the new words at their new places in the screen + dsiplays the title
    
        Stereotype: 
            Service Provider

        Arguments:
            delta_time
            
        """
        
        arcade.start_render()
        arcade.draw_text(self.SCREEN_TITLE, 300, 900, arcade.color.WHITE, 50)

    
        self.new_words(self.word_list[0], 0, 0, delta_time)
        self.new_words(self.word_list[1], 50, 1, delta_time)
        self.new_words(self.word_list[2], 100, 2, delta_time)
        self.new_words(self.word_list[3], 150, 3, delta_time)
        self.new_words(self.word_list[4], 200, 4, delta_time)

    
    def new_words(self, word, x_modifier, new_color, delta_time):
        
        if new_color == 0:
            self.changing_x0 += self.changing_d0 * delta_time
            arcade.draw_text(word, self.changing_x0 + x_modifier, 300, arcade.color.WHITE, 20)
            if self.changing_x0 < (0 - x_modifier) or self.changing_x0 > (self.SCREEN_WIDTH - (185 + x_modifier)):
                self.changing_d0 *= -1
        elif new_color == 1:
            arcade.draw_text(word, self.changing_x1 + x_modifier, 400, arcade.color.RED, 20)
            self.changing_x1 += self.changing_d1 * delta_time
            if self.changing_x1 < (0 - x_modifier) or self.changing_x1 > (self.SCREEN_WIDTH - (185 + x_modifier)):
                self.changing_d1 *= -1
        elif new_color == 2:
            self.changing_x2 += self.changing_d2 * delta_time
            arcade.draw_text(word, self.changing_x2 + x_modifier, 500, arcade.color.BLUE, 20)
            if self.changing_x2 < (0 - x_modifier) or self.changing_x2 > (self.SCREEN_WIDTH - (185 + x_modifier)):
                self.changing_d2 *= -1
        elif new_color == 3:
            self.changing_x3 += self.changing_d3 * delta_time
            arcade.draw_text(word, self.changing_x3 + x_modifier, 600, arcade.color.GREEN, 20)
            if self.changing_x3 < (0 - x_modifier) or self.changing_x3 > (self.SCREEN_WIDTH - (185 + x_modifier)):
                self.changing_d3 *= -1
        elif new_color == 4:
            self.changing_x4 += self.changing_d4 * delta_time
            arcade.draw_text(word, self.changing_x4 + x_modifier, 700, arcade.color.YELLOW, 20)
            if self.changing_x4 < (0 - x_modifier) or self.changing_x4 > (self.SCREEN_WIDTH - (185 + x_modifier)):
                self.changing_d4 *= -1
        


# tester
# game = Display()
# game.render_game()