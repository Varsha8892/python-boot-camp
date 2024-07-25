my_list=list(map(int,input().split()))
choice=int(input())
if choice==1:
    print(my_list.append())
    print(my_list)
elif choice==2:
    print(my_list.pop())
    print(my_list)
elif choice==3:
    print(my_list.sort())
    print(my_list)
else:
    print(len(my_list))  
    print(my_list)