# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

myString = "thisIsMyString"


def solution(s):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newString = []
    for char in s:
        if char in capitals:
            newString.append(s)
            newString.append(" ")
            newString.append(char)
    s = "".join(newString)
    return s


print(solution(myString))
