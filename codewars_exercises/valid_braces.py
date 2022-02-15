# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

# my version, this works for a string that only contains correct or incorrect pairs, but
# doesn't work for one that includes both correct and incorrect strings. Returns true but should return false
def validBraces(string):
    acceptable_pairs = ["()", "[]", "{}"]
    for x in acceptable_pairs:
        if x in string:
            return True
    return False


# solution 2
def validBraces2(string):
    square_brackets = "[]"
    curley_brackets = "{}"
    parentheses = "()"
    # double negative in this loop
    # while 1 of three specified texts is still findable, continue loop
    while (
        (string.find(square_brackets) != -1)
        or (string.find(curley_brackets) != -1)
        or (string.find(parentheses) != -1)
    ):
        # check matching pairs can be found in the string, and if they can remove them
        # only non-matching pairs will be left e.g [) will be left in string
        if string.find(square_brackets) != -1:
            string = string.replace(square_brackets, "")
        if string.find(curley_brackets) != -1:
            string = string.replace(curley_brackets, "")
        if string.find(parentheses) != -1:
            string = string.replace(parentheses, "")
    # the length is string is returned as a number
    # the not logical operator inverts the number's truthyness
    # 0 will be returned as True and anything else as False
    return not len(string)


# notes on not - any value other than zero is truthy, so not value inverts it - so not 1 or not -1 is False
# and not 0 is True
# print(not 1)
# print(not 0, not -1)
# https://www.w3schools.com/python/ref_keyword_not.asp

print(validBraces("())({}}{()][]["))

print(validBraces("()"))

print(validBraces("[)"))


def validBraces3(string):
    while "()" in string or "{}" in string or "[]" in string:
        string = string.replace("()", "")
        string = string.replace("{}", "")
        string = string.replace("[]", "")
    return False if len(string) != 0 else True
