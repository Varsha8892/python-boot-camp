my_list = list(map(int, input(" ").split()))
maxi = my_list[0]
mini = my_list[0]

for i in range(0, len(my_list)):
    if maxi < my_list[i]:
        maxi = my_list[i]
    if mini > my_list[i]:
        mini = my_list[i]

print("Maximum:", maxi)
print("Minimum:", mini)

avg = (maxi + mini) / 2

for i in range(len(my_list)):
    my_list[i] = avg

print("Modified list:", my_list)


