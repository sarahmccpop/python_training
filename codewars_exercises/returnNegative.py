# https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0


def make_negative(number):
    # ...
    if number > 0:
        return -abs(number)
    elif number <= 0:
        return number


print(make_negative(3))
print(make_negative(-31))
print(make_negative(0))
