#input=ABC
#output=XYZ
a="ABC"
b=" "
for i in a:
  b=(b+chr(ord(i)+23))
print(b)