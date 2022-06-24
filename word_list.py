from random import randint

class word_list:
    # Contains a list of words to be used in the game.
    # The list is randomly chosen from.
    
    def __init__(self):
        # define variables to be used throughout the program
        self.word_list = []
        self.guess_word = ""
        self.blank_list = []

    def random_word(self):
        # randomly choose a word from the list
        # return the word
        self.word_list = ["class", "method", "function", "variable", "comment", "program", "python", "jumper", "readme"]
        self.guess_word = self.word_list[randint(0, len(self.word_list)-1)]
        return self.guess_word

    def blank_word(self, guess_word):
        # return a blank word
        for i in range(len(guess_word)):
            self.blank_list.append("_")

        return self.blank_list

    def reveal_letter(self, guess_word, user_guess):
        # reveal the letter in the word
        for i in range(len(guess_word)):
            if guess_word[i] == user_guess:
                self.blank_list[i] = user_guess

        return self.blank_list