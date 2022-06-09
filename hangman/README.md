Hangman Project README

Assigned project to create 'Hangman' game. Introduction to Python programming including creation of classes and methods and calling these functions.


Milestone 1

Created the 'ask_letter' function as a method within 'Hangman' Class. Iteratively prompts the user for a one letter input using a 'while' loop, performing checks on whether the input is valid and then calls the 'check_letter' function:

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



Milestone 2

Set up the _init_ function as a method within 'Hangman' Class which prints two opening statements for the game and defines various variables used in the game, including '.num_lives', which defines the number of lives the player has and '.num_letters' which records the number of untried unique letters left in the word. These two variable define the loss and win condition of the game respectively when either reach zero.:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters\n")
        print(self.word_guessed, "\n")


Milestone 3

Created the 'check_letter' function as a method within the 'Hangman' Class which checks whether the letter is in the word and decreases .num_letters value by 1 or .num_lives value by 1 depending on whether the letter is in the word or not respectively:

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
                
Also added a call to ask_letter() method within the 'play_game' function. This function exists outside the Hangman class and is used to trigger the start of the game (runs when _name_ == 'main'). 

Conclusions

Happy with code as game runs exactly as desired. Was able to add basic visualisation of the hangman, though the coding for this was a series of If,Elif statements that could most likely be written more optimally:

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

Improvements to the game could include the user being able to import their own word list and also be able to set a difficulty rating. 
