import arcade
from game.settings import Settings

class Display():
    """Outputs the game state. The responsibility of the class is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        
    """

    def __init__(self):   
        #maybe get these from settings.py?
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        self.SCREEN_TITLE = "Welcome to SPEED"
        self.RADIUS = 150
    

    def render_game(self, score, word_list):
        arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        #display score
        #display each word in word_list
        #display buffer
        arcade.finish_render()
        arcade.run()


    

#Test Arcade refrence

# import arcade

# # Constants
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 960
# SCREEN_TITLE = "Welcome to Arcade"
# RADIUS = 150

# # Open the window
# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# # Set the background color
# arcade.set_background_color(arcade.color.BLACK)

# # Clear the screen and start drawing
# arcade.start_render()