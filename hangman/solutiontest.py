
import random

class Hangman:
    

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.word_guessed.extend("_" for i in range(len(self.word)))
        self.num_letters = len(set(self.word))
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)
        pass

    def check_letter(self, letter):
        if letter in self.word:
            self.num_letters -= 1

            for index, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[index] = letter

            print (f'Nice! {letter} is in the word!')       
            print (self.word_guessed)
            if self.num_letters == 0:
                print ('Congratulations! You won!')
        else:
            self.num_lives -=1
            print (f'Sorry {letter} is not in the word.')
            if self.num_lives == 0:
                print (f'You ran out of lives. The word was {self.word}.')
            else:
                print (f'You have {self.num_lives} lives left.')
                print (self.word_guessed)
                
        pass

    def ask_letter(self):
        while self.num_lives > 0 and self.num_letters > 0:
            letter = input("Please enter a single letter: ").lower()
            
            if len(letter) != 1:
                print("Please enter just one character")
            
            elif letter in self.list_letters:
                print(f'{letter} was already tried')
           
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)       
        
        pass


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)







