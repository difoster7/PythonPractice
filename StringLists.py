# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

in_str = input("Please input a string: ")
pali = True

first_half = in_str[: len(in_str)//2]

if len(in_str) % 2 == 0:
    second_half = in_str[len(in_str)//2 :]
else:
    second_half = in_str[len(in_str)//2 + 1 :]

for i in range(len(first_half)):
    if first_half[i] != second_half[len(second_half) - i - 1]:
        pali = False

if pali:
    print(in_str + " is a palindrome!")
else:
    print(in_str + " is not a palindrome!")

