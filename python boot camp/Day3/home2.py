#find the greatest of three numbers:
my_list = list(map(int, input("  ").split()))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")

