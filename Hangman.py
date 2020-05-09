import random


class HangmanGame:
    words_list = ["Machine", "House", "Car", "Money", "Garden", "Mobile", "Carrot"]
    selected_word = ""
    current_word = ""
    letter = ""
    entered_letters = []
    number_of_tries = 0

    def start_game(self):
        self.welcome_player()
        self.choose_word()
        self.print_number_of_letters()
        self.enter_letter()
        self.check_letter()

    def welcome_player(self):
        print("Hello! You started a Hangman game!")

    def choose_word(self):
        random_number = random.randint(0,len(self.words_list) - 1)
        self.selected_word = self.words_list[random_number]
        self.number_of_tries = len(self.selected_word) - 1
        self.current_word = "_" * len(self.selected_word)

    def print_number_of_letters(self):
        number_of_letters = len(self.selected_word)
        print("There are " + str(number_of_letters) + " letters in the word")
        print("_"*number_of_letters)

    def enter_letter(self):
        self.letter = input("Please, enter a letter ")

    def check_letter(self):
        is_letter_guessed = False
        if self.letter.lower() in self.entered_letters:
            print("You have already entered this letter. Try another one.")
            is_letter_guessed = True
        else:
            self.entered_letters += self.letter.lower()
            # check if user guessed the letter
            for index, character in enumerate(self.selected_word):
                if self.letter.lower() == character.lower():

                    # if user guessed replace "_" with this letter
                    self.current_word = self.current_word[:index] + self.letter.lower() + self.current_word[index + 1:]
                    is_letter_guessed = True

        if is_letter_guessed:
            print(self.current_word)
            if not self.end_game():
                self.enter_letter()
                self.check_letter()
        else:
            self.number_of_tries -= 1
            if not self.end_game():
                print("Try more")
                self.enter_letter()
                self.check_letter()

    def end_game(self):
        if self.current_word.lower() == self.selected_word.lower():
            print ("You guessed the word.")
            return True
        elif self.number_of_tries == 0:
            print("The game is over. Try again")
            return True
        else:
            return False


game = HangmanGame()
game.start_game()
