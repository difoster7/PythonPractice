# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for n in a:
    if n < 5:
        b.append(n)

print(b)

print("one line")

print([n for n in a if n < 5])

print("input")

i = input("Choose a number: ")
print([n for n in a if n < int(i)])