#find second max element in array:
my_list = list(map(int, input("  ").split()))
def find_second_max(arr):
    max_val = second_max = float('-inf')
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max and num != max_val:
            second_max = num
    return second_max

