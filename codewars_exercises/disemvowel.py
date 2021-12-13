#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
# version 1 my solution
myString = 'THIS IS MY STRING'
myString2 = "My name is Sarah"

def disemvowel(string_):
    vowels = 'aeoiuAEOIU'
    newString = []
    for char in string_:
        if char not in vowels:
            newString.append(char)

    string_ = "".join(newString) #specify what will be between letters when joined
    return string_
print(disemvowel(myString))
print(disemvowel(myString2))

def disemvowel2(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i, "")
    return string_

print(disemvowel2(myString))
print(disemvowel2(myString2))
