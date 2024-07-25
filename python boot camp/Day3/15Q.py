my_list = list(map(int, input("  ").split()))
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)





