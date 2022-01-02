# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def reverse(fwd_str):
    split_str = fwd_str.split()
    return " ".join(split_str[::-1])


str = "My name is David"
print(reverse(str))
