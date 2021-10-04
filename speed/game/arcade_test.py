# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_text("word1",120.0,500.0,arcade.color.GREEN,40,80,'left')
arcade.draw_text("word2",120.0,400.0,arcade.color.PURPLE,40,80,'left')
arcade.draw_text("word3",120.0,300.0,arcade.color.ORANGE,40,80,'left')
arcade.draw_text("word4",120.0,200.0,arcade.color.CYAN,40,80,'left')
arcade.draw_text("word5",120.0,100.0,arcade.color.AUBURN,40,80,'left')



# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()