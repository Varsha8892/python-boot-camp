arr=list(map(int,input().split(" ")))
count=0
for i in range (1,len(arr)-1):
 if(arr[1]>=arr[i-1]) and (arr[i]>arr[i+1]):
    count=i
       # print(arr[i],end=" ")
if(arr[-1>arr[-2]] and arr[-1]>count):
 count+-len(arr)-1
 print(arr[count])