


class AnswerCheck:
    """Handles if answer is correct.
    
    Stereotype: 
        Service Provider

    Attributes:
        
        
    """

    def __init__(self):
            
        self.word_list = []


    def check_answer(self, word_list, new_word, scoreboard):
        for x in len(word_list):
            if new_word == word_list[x]:
                word_list.remove(word_list[x])
                score = scoreboard.return_score()
        return score
