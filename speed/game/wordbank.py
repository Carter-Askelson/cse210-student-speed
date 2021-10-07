import random
from pathlib import Path

class WordBank:
    """handles generating words
    
    Stereotype:
        Information Holder
    Attributes:
        
        
    """

    def __init__(self):
        self.words_list = []
        #print(self.get_words()) #uncomment to view results of get_words

    def get_words(self):
        #get the next number of words from word.txt
        word_file = Path(__file__).parent / "words" / "words.txt"
        if not word_file.exists():
            raise ValueError(f"Word file not found: words.txt")

        i = 0
        while i < 5:
            lines = open(word_file).read().splitlines()
            self.words_list.append(random.choice(lines))
            i += 1
        return self.words_list