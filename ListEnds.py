# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

def list_end(input_list):
    return [input_list[0], input_list[len(input_list) - 1]]

a = [5, 10, 15, 20, 25]
print(list_end(a))