from director import new_word

from speed.game.Scoreboard import Scoreboard


class answercheck():
    """Handles if answer is correct.
    
    Stereotype:
        Service Provider

    Attributes:
        
        
    """

    def __init__(self):
            
        self.word_list = []


    def update_word_list(self, wordlist):
        self.word_list = wordlist

    def check_answer(self, new_word):
        if new_word in self.word_list:
            #increase score
            #print success in usermessages
            #director.stargame() or newround()?
            pass
        else:
            #print incorrect in usermessages
            pass
