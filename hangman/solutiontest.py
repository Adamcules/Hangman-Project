
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
        print(f"The mystery word has {len(self.word)} characters\n")
        print(self.word_guessed, "\n")


    def check_letter(self, letter):
        if letter in self.word:
            self.num_letters -= 1

            for index, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[index] = letter

            print (f'Nice! {letter} is in the word!\n')       
            print (self.word_guessed, "\n")
            if self.num_letters == 0:
                print ('Congratulations! You won!\n')
        else:
            self.num_lives -=1
            print (f'Sorry {letter} is not in the word.\n')
            if self.num_lives == 0:
                print ("   O  \n", "/", "¦", "\\\n", " /", "\\\n")
                print (f'You ran out of lives. The word was {self.word}.\n')
            else:
                if self.num_lives == 4:
                    print ("   O   \n")
                elif self.num_lives == 3:
                    print ("   O  \n", "/\n")
                elif self.num_lives == 2:
                    print ("   O  \n", "/", "¦\n")
                elif self.num_lives == 1:
                    print ("   O  \n", "/", "¦", "\\\n")
                print (f'You have {self.num_lives} lives left.\n')
                print (self.word_guessed, "\n")
                


    def ask_letter(self):
        while self.num_lives > 0 and self.num_letters > 0:
            letter = input("Please enter a single letter: ").lower()

            if len(letter) != 1:
                print("Please enter just one character\n")
            
            elif letter in self.list_letters:
                print(f'{letter} was already tried\n')
           
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)        


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)







