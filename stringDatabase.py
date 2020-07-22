"""
   A class used to represent a Database of four letters word

   ...

   Attributes
   ----------
   list_content : list
       keeps all the word in a list

   Methods
   -------
   random_word_pick()
        this method generates a random number between 0 and 4029 as mentioned in the assignment descriptions and pick a word
   """

import random


class IO:

    def __init__(self, list_content=[], word=" "):
        file = open("four_letters.txt", "r")
        content = file.read()
        self.list_content = content.split()
        self.word = word
        file.close()

    # This function generates a random number between 0 and 4029 as mentioned in the assignment descriptions and pick
    # a word

    def random_word_pick(self):
        for x in range(1):
            number = random.randint(0, 4029)
        self.word = self.list_content[number]
        self.list_content.remove(self.word)
