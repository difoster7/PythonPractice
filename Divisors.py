# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

num = int(input("Enter a number: "))

divs = [n for n in range(1, num) if num % n == 0]

print(divs)
