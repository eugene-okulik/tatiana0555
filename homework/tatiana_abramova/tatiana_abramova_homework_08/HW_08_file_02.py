import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def element_fibonacci(n):
    global fib_num
    fib_gen = fibonacci_numbers()
    for _ in range(n + 1):
        fib_num = next(fib_gen)
    return fib_num


fib_numbers = [5, 200, 1000, 100000]
fib_results = {n: element_fibonacci(n) for n in fib_numbers}

for n, fib_num in fib_results.items():
    print(f"{n}-е число Фибоначчи: {fib_num}")
