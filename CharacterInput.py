from datetime import date

name = input("What is your name? ")
age = int(input("What is your age? "))

repeat = int(input("Prints? "))

print(name + " is " + str(age) + " years old.")

current_year = date.today().year

full_string = ""
add_string = "They will be 100 in " + str(current_year + 100 - age) + "."

for i in range(repeat):
    full_string = full_string + add_string + "\n"
#    print("They will be 100 in " + str(current_year + 100 - age) + ".")

print(full_string)