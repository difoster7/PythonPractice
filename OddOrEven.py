# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

if int(num1) % int(num2) == 0:
    print(num1 + " is divisible by " + num2)
else:
    print("The remained of " + num1 + " divided by " +
          num2 + " is " + str(int(num1) % int(num2)) + ".")

# if int(num) == 4:
#     print("You chose 4!")
# elif int(num) % 2 == 0:
#     print(num + " is even!")
# else:
#     print(num + " is odd!")
