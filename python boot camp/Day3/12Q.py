my_list=list(map(int,input().split()))
mini=my_list[3]
for i in range(len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
        print(mini)
