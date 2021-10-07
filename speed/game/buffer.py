import arcade

class Buffer(arcade.Window):
    """Detects player input.

    Stereotype: 
        Service Provider

    Attributes:
        
        
    """

    def __init__(self):#self, width, height, words, word_rows_count=20):
        #super().__init__(width, height, title="Space Typer")
        self.user_input = ""
        self.keep_playing = True

    def on_key_press(self, key):
        
        """Gets the letter that was typed.

        Args:
            self (InputService): An instance of InputService.

       Returns:
            string: The letter that was typed.
       """
        while key != arcade.key.ENTER and self.keep_playing == True:
            if key == arcade.key.Q:
                self.user_input += "q"
            elif key == arcade.key.W:
                self.user_input += "w"
            elif key == arcade.key.E:
                self.user_input += "e"
            elif key == arcade.key.R:
                self.user_input += "r"
            elif key == arcade.key.T:
                self.user_input += "t"
            elif key == arcade.key.Y:
                self.user_input += "y"
            elif key == arcade.key.U:
                self.user_input += "u"
            elif key == arcade.key.I:
                self.user_input += "i"
            elif key == arcade.key.O:
                self.user_input += "o"
            elif key == arcade.key.P:
                self.user_input += "p"
            elif key == arcade.key.A:
                self.user_input += "a"
            elif key == arcade.key.S:
                self.user_input += "s"
            elif key == arcade.key.D:
                self.user_input += "d"
            elif key == arcade.key.F:
                self.user_input += "f"
            elif key == arcade.key.G:
                self.user_input += "g"
            elif key == arcade.key.H:
                self.user_input += "h"
            elif key == arcade.key.J:
                self.user_input += "j"
            elif key == arcade.key.K:
                self.user_input += "k"
            elif key == arcade.key.L:
                self.user_input += "l"
            elif key == arcade.key.Z:
                self.user_input += "z"
            elif key == arcade.key.X:
                self.user_input += "x"
            elif key == arcade.key.C:
                self.user_input += "c"
            elif key == arcade.key.V:
                self.user_input += "v"
            elif key == arcade.key.B:
                self.user_input += "b"
            elif key == arcade.key.N:
                self.user_input += "n"
            elif key == arcade.key.M:
                self.user_input += "m"
            elif key == arcade.key.ESCAPE:
                self.keep_playing = False
                break
            else:
                self.user_input += ""
        
            

    # if ESC pressed:
    # sys.exit()

    # elif ENTER pressed
    # terminal clear()
    # self.answerchecker.check_answer(self.new_word)

    # else
    # self.new_word += new_letter

# Legacy Code from template

# import sys
# from asciimatics.event import KeyboardEvent

# class InputService:
#     """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

#     Stereotype: 
#         Service Provider

#     Attributes:
#         _screen (Screen): An Asciimatics screen.
#     """

#     def __init__(self, screen):
#         """The class constructor.

#         Args:
#             self (InputService): An instance of InputService.
#         """
#         self._screen = screen

#     def get_letter(self):
#         """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

#         Args:
#             self (InputService): An instance of InputService.

#         Returns:
#             string: The letter that was typed.
#         """
#         result = ""
#         event = self._screen.get_key()
#         if not event is None:
#             if event == 27:
#                 sys.exit()
#             elif event == 10: 
#                 result = "*"
#             elif event >= 97 and event <= 122: 
#                 result = chr(event)
#         return result
