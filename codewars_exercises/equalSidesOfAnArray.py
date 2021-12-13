# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python

# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
# the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

# For example:
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

# Note:
# If you are given an array with multiple answers, return the lowest correct index.


def find_even_index(arr):
    right_sum = 0
    left_sum = 0
    loop_number = 0
    for number in arr:
        number = int(number)
        right_numbers = arr[(loop_number + 1) :]
        # right_numbers = arr[(arr.index(number) + 1) :] this finds the FIRST index of a number and start the slice from there so tests fail on arrays with duplicate numbers as it begins from first occurance of this number
        left_numbers = arr[:loop_number]

        right_sum = sum(right_numbers)
        left_sum = sum(left_numbers)
        # print(
        #     "Whole array: ",
        #     arr,
        #     "Number is: ",
        #     number,
        #     "Left numbers: ",
        #     left_numbers,
        #     "Left sum:",
        #     left_sum,
        #     "Middle number value: ",
        #     number,
        #     "Right numbers: ",
        #     right_numbers,
        #     "Right sum: ",
        #     right_sum,
        # )

        if left_sum == right_sum:
            return loop_number
        loop_number = loop_number + 1

    # print(right_sum, left_sum)
    if right_sum != left_sum:
        return -1
    else:
        return loop_number


# print(find_even_index([1, 2, 3, 4, 5]))
# print(find_even_index([1, 2, 3, 4, 5, 4, 3, 2, 1]))

# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
print(find_even_index([1, 2, 3, 4, 3, 2, 1]))

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index
# ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
print(find_even_index([1, 100, 50, -51, 1, 1]))  # should return 1

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))  # should return 0
print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # should return 3
print(find_even_index([20, 10, 30, 10, 10, 15, 35]))  # should return index 3
