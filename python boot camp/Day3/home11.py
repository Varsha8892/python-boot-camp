#check wheather number palamindore are not using while loop:
my_list = list(map(int, input().split()))
def sum_of_squares_of_digits(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit ** 2
        else:
            odd_sum += digit ** 2
        n //= 10
    return even_sum, odd_sum

