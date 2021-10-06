import arcade
import random
from .settings import Settings

class Display:
    """Outputs the game state. The responsibility of the class is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        
    """

    def __init__(self):
        self.game_settings = Settings()

    def render_game(self, score, word_list):
        arcade.open_window(self.game_settings.SCREEN_WIDTH,
                           self.game_settings.SCREEN_HEIGHT,
                           self.game_settings.SCREEN_TITLE,
                           self.game_settings.RADIUS)
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        self.draw_score()
        text_sprites_list = self.create_text_sprites(word_list)
        text_sprites_list.draw()


        # display score
        # display each word in word_list
        # display buffer
        arcade.finish_render()
        arcade.run()

    def create_text_sprites(self, word_list):
        temp_sprite_list = arcade.SpriteList()
        for word in word_list:
            temp_sprite_list.append(arcade.create_text_sprite(word,
                                                              random.randint(100, 850),
                                                              random.randint(100, 850),
                                                              arcade.color.WHITE, 18))
        return temp_sprite_list

    def draw_score(self):
        score_text = f"Score: {0}"
        arcade.draw_text(score_text, 8, 936, arcade.csscolor.WHITE, 18)


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