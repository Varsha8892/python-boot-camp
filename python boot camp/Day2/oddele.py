my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list),2):
    if (i%2==0):
        even+=1
    else:
        odd+=1
        print(even,odd)    
