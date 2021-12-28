# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

keep_playing = True
num_games = 0
total_guesses = 0

while keep_playing:

    num_games += 1
    game_over = False
    num_guesses = 0
    random_num = random.randint(1, 10)

    while not game_over:

        num_guesses += 1
        guess = input("Guess a number between 1 and 10, or type exit: ")

        if guess == "exit":
            game_over = True
            keep_playing = False
        else:
            if int(guess) == random_num:
                game_over = True
                total_guesses += num_guesses
                print("Correct! The number was " + str(random_num))
                print("You needed " + str(num_guesses) + " guesses.")
                keep_playing_str = input("Would you like to play again (y/n)?")

                if keep_playing_str == "n" or keep_playing_str == "no":
                    keep_playing = False
            elif int(guess) > random_num:
                print("Too high, guess again!")
            else:
                print("Too low, guess again!")

print("You played " + str(num_games) + " games.")
print("It took you an average of " + str(total_guesses/num_games) + " guesses each game.")
