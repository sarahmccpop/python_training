#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

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
