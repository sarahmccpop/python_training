# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python


def square_sum(numbers):
    newNumbers = []
    my_sum = 0
    for num in numbers:
        squaredNum = num * num
        newNumbers.append(squaredNum)
        print(newNumbers)
        my_sum = sum(newNumbers)
        print(my_sum)
    return my_sum


square_sum([2, 3, 2])

# one liner
def square_sum2(numbers):
    return sum(num ** 2 for num in numbers)


print("One liner is ", square_sum2([2, 3, 2]))
