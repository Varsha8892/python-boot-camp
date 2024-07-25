k = int(input("Enter k: "))
n = int(input("Enter n: "))
my_list = list(map(int, input("Enter the list (space-separated): ").split()))
if k + n > len(my_list):
    print("Error")
else:
    print(my_list[k+n])