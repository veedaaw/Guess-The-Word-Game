"""
   A class used to represent a Game

   ...

   Attributes
   ----------
   number : int
        a Static variable to store number of object of this class
   letter_freq : dict
        this dictionary contains frequency of each letters, used for score calculation
   word_to_guess : str
        this the word that players have to guess for each round of the game
   current_guess : str
        the current guess of the player, initially begins with ----
   score : int
       total scoring of the current game
   status : str
        keeps the status of the game, either success, gave up or failed
   bad_guess : int
        number of bad guesses
   right_guess : int
        number of right guesses
   missed_letters : int
        number of missed letters
   correct_letters : list
        number of correct letters that user has found so far
   XP: int
         XP is an additional element to calculate the score
   Methods
   -------
   modify_guess(letter)
       modifies the current guess based on user's input
   calMissedLetters()
       calculation of Missed Letters
   calcScore()
        calculation of score for a simple game
   """
class Game:

    # Static variable to store number of object of this class
    number = 0;

    # This dictionary contains frequency of each letters, used for score calculation
    letter_freq = {"a": 8.1, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.7, "f": 2.23, "g": 2.02, "h": 6.09, "i": 6.97,
                   "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41
        , "n": 6.75, "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06, "u": 2.76, "v": 0.98, "w": 2.36,
                   "x": 0.15, "y": 1.97, "z": 0.07}

    def __init__(self, word_to_guess, current_guess="----", score=0, status="lost", bad_guess=0, missed_letters=0,
                 right_guess=0, correct_letters=[], XP=0):
        self.word_to_guess = word_to_guess
        self.current_guess = current_guess
        self.score = score
        self.status = status
        self.bad_guess = bad_guess
        self.missed_letters = missed_letters
        self.right_guess = right_guess
        self.correct_letters = correct_letters
        # XP is an additional element to calculate the score
        self.XP = XP
        Game.number += 1

    # This function modifies the current guess based on user's input
    def modify_guess(self, letter):

        # Find all occurrences of a specific letter
        occurrences = self.word_to_guess.count(letter)

        indices = [i for i, g in enumerate(self.word_to_guess) if g == letter]
        self.right_guess += len(indices)

        # String to List
        self.current_guess = list(self.current_guess)
        self.word_to_guess = list(self.word_to_guess)

        # Get index of the letter
        for index in indices:
            self.current_guess[index] = letter

        # List to String
        self.current_guess = ''.join(self.current_guess)
        self.word_to_guess = ''.join(self.word_to_guess)

    # Calculation of Missed Letters
    def calMissedLetters(self):
        self.missed_letters = 4 - self.right_guess

    # Calculation of score for a simple game
    def calcScore(self):
        for word in self.correct_letters:
            self.score += Game.letter_freq[word]
            self.score = ((100 - self.score) / 100)
        self.score = (self.right_guess * 10) - (self.bad_guess * 2) + self.XP - (self.missed_letters * 2)
