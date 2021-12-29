# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def get_int(text="Please enter an integer: "):
    try:
        return int(input(text))
    except ValueError:
        print("Invalid input, please only enter integers.")


def fib(stop_len, fib_seq=[1]):
    if len(fib_seq) == stop_len:
        return fib_seq
    elif len(fib_seq) == 1:
        fib_seq.append(1)
        return fib(stop_len, fib_seq)
    else:
        fib_seq.append(fib_seq[len(fib_seq) - 2] + fib_seq[len(fib_seq) - 1])
        return fib(stop_len, fib_seq)


fib_len = get_int("Enter the number of Fibonacci digits to generate: ")
seq = fib(fib_len)
print(seq)
