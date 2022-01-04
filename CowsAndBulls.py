# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random


def get_int(text="Please enter an integer: "):
    try:
        return int(input(text))
    except ValueError:
        print("Invalid input, please only enter integers.")


def ran_four_digit():
    return random.randint(1, 9999)


def compare_thousands(answer, guess):
    if answer//1000 == guess//1000:
        return True
    else:
        return False


def compare_hundreds(answer, guess):
    answer %= 1000
    guess %= 1000
    if answer//100 == guess//100:
        return True
    else:
        return False


def compare_tens(answer, guess):
    answer %= 100
    guess %= 100
    if answer//10 == guess//10:
        return True
    else:
        return False


def compare_ones(answer, guess):
    answer %= 10
    guess %= 10
    if answer == guess:
        return True
    else:
        return False


if __name__ == "__main__":
    keep_playing = True
    while keep_playing:

        ran_num = random.randint(1, 9999)
        user_guess = get_int("Guess a number between 1-9999: ")

        game_over = False
        num_guesses = 1

        while not game_over:
            cows_are_true = []
            if ran_num == user_guess:
                print('Congratulations! The number was ' + str(ran_num))
                print("It took you " + str(num_guesses) + " guesses.")
                keep_playing_input = input("Would you like to play again? (y/n)")
                if keep_playing_input == "n" or keep_playing_input == "no":
                    keep_playing = False
                game_over = True
            else:
                cows_are_true.append(compare_thousands(ran_num, user_guess))
                cows_are_true.append(compare_hundreds(ran_num, user_guess))
                cows_are_true.append(compare_tens(ran_num, user_guess))
                cows_are_true.append(compare_ones(ran_num, user_guess))

                print(str(cows_are_true.count(True)) + ' cows, ' + str(cows_are_true.count(False)) + ' bulls')

                user_guess = get_int("Guess a new number: ")
                num_guesses += 1

