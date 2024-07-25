#find the peak element in an array:
my_list = list(map(int, input("  ").split()))
def find_peak(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[-1] >= arr[-2]:
        return arr[-1]
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]


