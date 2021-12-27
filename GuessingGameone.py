# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

keep_playing = True

while keep_playing:
    random_num = random.randint(10)

    guess = input("Guess a number between 1 and 10, or type exit: ")

    if input == "exit":
        break
    else:
        if int(input) == random_num:
            print("Correct! The number was " + str(random_num))
            keep_playing_str = input("Would you like to play again (y/n)?")
            if keep_playing_str == "n" or keep_playing_str == "no"
        elif int(input) > random_num:
            print("Too high, guess again!")
        else:
            print("Too low, guess again!")