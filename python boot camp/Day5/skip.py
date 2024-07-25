#input=ABC
#output=EFG
a="ABC"
b=" "
for i in a:
  b=(b+chr(ord(i)+4))
print(b)


