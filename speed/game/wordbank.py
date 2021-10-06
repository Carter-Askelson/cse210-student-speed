import random

class WordBank():
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
        i = 0
        while i < 5:
            lines = open('speed\game\words.txt').read().splitlines()
            self.words_list.append(random.choice(lines))
            i += 1
        return self.words_list


    def return_words(self):
        self.get_words()
        return self.word_list

#WordBank().get_words() #uncomment to view results of get_words
