
import random

class Hangman:
    

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.word_guessed.extend("_" for i in range(len(self.word)))
        self.num_letters = 
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)
        pass

    def check_letter(self, letter) -> None:
        pass

    def ask_letter(self):
        while 2 > 1:
            letter = input("Please enter a single letter: ")
            if len(letter) != 1:
                print("Please enter just one character")
            
            elif letter in self.list_letters:
                print(f'{letter} was already tried')
           
            else:
                self.list_letters.append(letter)
                print(*self.list_letters)
        
        
        pass


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)







