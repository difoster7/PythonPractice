# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

def get_choice(player):
    print("Player " + player + " please choose rock, paper, or scissors.")
    input_valid = False
    while not input_valid:
        choice = input("Enter 1 for rock, 2 for paper, or 3 for scissors: ")
        if choice == "1" or choice == "2" or choice == "3":
            input_valid = True
    return int(choice)

while True:
    player1 = get_choice("1")
    player2 = get_choice("2")

    if player1 == player2:
        print("Tie game!")
    elif (player2 == player1 - 1) or (player1 == 1 and player2 == 3):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play_again = input("Would you like to play again? (y/n)")

    if play_again == "n" or play_again == "no":
        break
