# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

s = "My names is Sarah"
t = "what a nice day"


def remove_char(s):
    s = s[1:-1]
    return s


print(remove_char(s))
print(remove_char(t))
