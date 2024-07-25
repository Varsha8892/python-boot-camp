my_list=list(map(int,input().split()))
maxi=my_list[3]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
        print(maxi)
