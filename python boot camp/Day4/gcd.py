arr=list(map(int,input().split(" ")))
a=int(input("enter the 1st number:"))
b=int(input("enter the 2st number:"))
while b!=0:
    a,b=b,a%b
    print("gcd of two number is:",a)
