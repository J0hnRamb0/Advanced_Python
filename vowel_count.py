user = input("enter your statement: ")

vowel={"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0,}        

for i in user:
    if i in vowel:
        vowel[i] += 1

print(vowel)



