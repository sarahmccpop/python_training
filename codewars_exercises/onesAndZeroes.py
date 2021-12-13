# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.


def binary_array_to_number(arr):
    # first join all array together to make a binary code string
    # some function to convert binary to int
    new_array = []
    for num in arr:
        string_num = str(num)
        new_array.append(string_num)
    arr = "".join(new_array)
    return int(arr, 2)


one = [0, 0, 0, 1]
five = [1, 0, 1]
thirteen = [1, 1, 0, 1]
print(binary_array_to_number(one))
print(binary_array_to_number(five))
print(binary_array_to_number(thirteen))


def binary_array_to_number2(arr):
    return int("".join(map(str, arr)), 2)


print(binary_array_to_number2(one))
print(binary_array_to_number2(five))
print(binary_array_to_number2(thirteen))
