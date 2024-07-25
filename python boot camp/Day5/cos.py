vowel="aeiou"
consenent="bcdfghijklmnopqrstuvwxy"
count=0
c=0
i="hello word"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
     if(i in consenent):
        count+=1
print(count)



        