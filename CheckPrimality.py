# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def get_int(text="Please enter an integer: "):
    try:
        return int(input(text))
    except ValueError:
        print("Invalid input, please only enter integers.")


def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


check_again = True
while check_again:
    num = get_int("Enter a number to check for primality: ")
    if check_prime(num):
        print(str(num) + " is a prime number!")
    else:
        print(str(num) + " is not a prime number :(")

    check_again_input = input("Would you like to check another number? (y/n)")
    if check_again_input == "n" or check_again_input == "no":
        check_again = False
