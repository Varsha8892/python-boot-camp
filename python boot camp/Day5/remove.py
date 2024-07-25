#reamove all the brackets from all the algerbic expression
n=input()
for i in n:
     if(ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
       pass
     else:
       print(i,end="")
print()