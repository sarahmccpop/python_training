# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

## my version
def square_digits(num):
    number = int("".join([str(int(x) ** 2) for x in str(num)]))
    print("number is ", number)
    print(type(number))
    return number


print(square_digits(22))
print(square_digits(81))
print(square_digits(9119))

## remember that this can be returned without being assigned
def square_digits2(num):
    return int("".join(str(int(x) ** 2) for x in str(num)))


print(square_digits2(81))
print(square_digits2(9119))
