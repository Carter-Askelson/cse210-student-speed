from asciimatics.screen import Screen
from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep
""" 
color key
COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7 
"""
""" 
attribute key
A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4
"""

""" def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("ASCIIMATICS", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)]) """

def demo():
    with ManagedScreen() as screen:
        A_BOLD = 1
        COLOUR_GREEN = 2
        screen.print_at('Hello world!', 0, 0, COLOUR_GREEN, A_BOLD)
        screen.print_at('Hello world!', 20, 0, COLOUR_GREEN)
        screen.refresh()
        sleep(10)

demo()