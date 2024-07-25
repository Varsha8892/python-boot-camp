
my_list= list(map(int, input(" ").split()))
n = int(input("Enter n: "))

sum_of_list = sum(my_list)
sum_of_natural_numbers = n * (n + 1) // 2

print("Difference:", sum_of_natural_numbers - sum_of_list)

