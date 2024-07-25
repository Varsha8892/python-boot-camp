#find the sum of squares of given numberss:
my_list = list(map(int, input().split()))
def sum_of_squares(numbers):
    return sum(num ** 2 for num in numbers)


