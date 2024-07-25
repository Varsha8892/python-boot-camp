#write a program to print first and fib series:
my_list = list(map(int, input().split()))
def print_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    print(fib_series)





