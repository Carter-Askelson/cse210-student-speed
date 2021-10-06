


class AnswerCheck:
    """Handles if answer is correct.
    
    Stereotype: 
        Service Provider

    Attributes:
        
        
    """

    def __init__(self):
            
        self.word_list = []


    def check_answer(self, new_word, scoreboard):
        for x in len(self.word_list):
            if new_word == self.word_list[x]:
                self.word_list.remove(self.word_list[x])
                score = scoreboard.return_score()
        return score
