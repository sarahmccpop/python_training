# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    else:
        return "No"


# option 2
# this method does not check if something is True, only if it is truthy so for example a 3 will return Yes
def bool_to_word2(boolean):
    return "Yes" if boolean else "No"


my_bool = 3
print(bool_to_word(my_bool))
print(bool_to_word2(my_bool))
