# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random


def strongest(length):
    password = []
    for x in range(length):
        password.append(chr(random.randint(33, 126)))
    return "".join(password)


def letters_only(length):
    password = []
    for x in range(length):
        random_num = random.randint(65, 116)
        if random_num > 90:
            random_num += 6
        password.append(chr(random_num))
    return "".join(password)


def letters_and_nums(length):
    password = []
    for x in range(length):
        random_num = random.randint(55, 116)
        if random_num < 65:
            random_num -= 7
        elif random_num > 90:
            random_num += 6
        password.append(chr(random_num))
    return "".join(password)


def weakest(length):
    pass_list = ("Monkey", "Dragon", "Football", "Sunshine", "Baseball", "Welcome", "Root", "Princess", "Mustang", "Bailey")
    password = []
    for x in range(length):
        password.append(random.choice((pass_list)))
    return "".join(password)


print(strongest(8))
print(letters_only(8))
print(letters_and_nums(8))
print(weakest(2))
