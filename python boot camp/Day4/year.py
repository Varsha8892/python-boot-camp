a=int(input("enter the year:"))
b=int(input("enter the year:"))
#for i in range(a,b):
#if (i%4==0)and(i%100!=0):
#  print(i)
if (a%400==0):
    print("leap year")
else:
    print("not a leap")