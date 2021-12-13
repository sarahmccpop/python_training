#https://www.codewars.com/kata/546f922b54af40e1e90001da/python

#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

#If anything in the text isn't a letter, ignore it and don't return it.

myString = 'a b c '
myString2 = "My name is Sarah"
myString3 = '!!!ZZZaaa&&%%'
def alphabet_position(text):
    dict = {'a': '1', 'b':'2', 'c' : '3', 'd':'4', 'e': '5', 'f':'6', 'g': '7',
            'h': '8', 'i': '9', 'j': '10', 'k' : '11', 'l': '12', 'm': '13', 'n':'14',
            'o': '15', 'p': '16', 'q': '17', 'r': '18', 's':'19', 't':'20', 'u':'21', 'v':'22',
            'w':'23', 'x':'24', 'y':'25','z':'26'}
    positionString =  []
    for char in text.lower():
        if char in dict:
            positionString.append(dict[char])

    return " ".join(positionString)

print(alphabet_position(myString))
print(alphabet_position(myString2))
print(alphabet_position(myString3))

# version 2 - released when submitted
def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
# reading on what this is and why it works - https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python/4528997    
# ord - accepts a string of length 1 as an argument and returns the unicode code point representation of the passed argument. For example ord('B') returns 66 which is a unicode code point value of character ‘B’. - https://beginnersbook.com/2019/03/python-ord-function/
# isalpha - used to check if a character is an alphabetic letter - returns true or false - https://www.w3schools.com/python/ref_string_isalpha.asp
# for every character (c) in a string (text CONVERTED to lower), if the character is alphabetic, find the ord of it and minus 96 from it. Parse that number to a string and join it to a string with a ' ' space in between. Return that 
print(alphabet_position2(myString))
print(alphabet_position2(myString2))
print(alphabet_position2(myString3))