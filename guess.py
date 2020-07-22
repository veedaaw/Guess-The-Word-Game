
"""
   The main class called Game used to represent a Game and it's start menu and other details

   ...

   Attributes
   ----------
   allGames : list
       keeps all the games in a list

   """

from game import Game
from stringDatabase import IO

# A list containing of all the games user played
allGames = []

# Game start here!
print("Welcome to The Great Guessing Game! ^_^" + "\n")

# Just to have a better look of the game, I added a start menu

############################### Start menu #####################################
while 1:

    print("|-----------------------START MENU-----------------------------|")
    print("|To start a new game press 's', to terminate the game press 't'|")
    print("|--------------------------------------------------------------|" + "\n")

    input1 = str(input())

    if input1 == "t":
        break
    elif input1 == "s":
        print("Game Number: " + str(Game.number + 1))

        # Instantiating of IO class
        io = IO()
        io.random_word_pick()

        # Instantiating of Game class
        game = Game(io.word)

        allGames.append(game)

############################### Actual game starts here ################################
    while 1:

        if game.current_guess == game.word_to_guess:
            print("**** Congratulation! You Won! ****")
            game.status = "Success"
            break

        print("Current Guess: " + game.current_guess)
        print("g = guess, t = tell me, l for a letter, and q to back to start menu")

        string = str(input())

############################### if input is l #####################################
        if string == "l":

            print("Enter a letter: ")
            string2 = str(input())

            if string2 not in game.word_to_guess or string2 == "":
                print("Oops! Incorrect letter! Try again!")
                game.bad_guess = game.bad_guess + 1

                continue
            else:

                print("Perfect! You found a letter!")
                game.modify_guess(string2)
                game.correct_letters.append(string2)
                continue
############################### if input is q #####################################
        elif string == "q":
            break
############################### if input is g #####################################
        elif string == "g":
            print("enter your guess: ")
            string3 = str(input())
            if string3 == game.word_to_guess:
                print("**** Congratulation! You Won! ****")

                correct = list(string3)
                game.correct_letters = correct
                game.right_guess = 4
                game.XP = game.XP + 20
                game.status = "Success"

                break
            else:
                print("Game Over! Correct word was: " + str(game.word_to_guess))
                game.bad_guess = 4 - game.right_guess
                game.XP = game.XP - 20
                game.status = "Failed"
                break
############################### if input is t #####################################

        elif string == "t":
            print("The word is: " + game.word_to_guess)
            print("Game Over!")
            game.status = "Gave up"
            game.XP = game.XP - 30
            break

        else:
            print("You have entered a wrong command")
            continue

########################### Game report section ##################################
    final_score = 0
    game.calcScore()

    print("---------------------------GAME REPORT-------------------------------" + "\n")
    print("Game      Status     Right Guesses     Bad Guesses    Missed Letters     Score")
    print("-----     ------    --------------     -----------    --------------    ------")

    for game in allGames:
        print(str(allGames.index(game) + 1) + "         " + str(game.status) + "             " + str(
            game.right_guess) + "               " +
              str(game.bad_guess) + "               " + str(4 - game.right_guess) + "          " + str(
            game.score) + "\n")
        final_score += game.score

    print("Final Score: " + str(final_score))

print("----------------------------------GOODBYE-----------------------------------------")
