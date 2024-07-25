#input=hello123
#output=6
check="123456789"
ans=0
i="hello 123"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)