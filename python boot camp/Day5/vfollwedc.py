#print all the vowels follwed by consenent
vowel="aeiou"
consenent="bcdfghijklmnopqrstuvwxy"
ans=""
i="hello word"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
     if(i in consenent):
        ans+=i
print(ans)