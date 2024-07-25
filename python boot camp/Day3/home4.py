#reverse an array without using the built-in reverse() function:
my_list = list(map(int, input("  ").split()))
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
