# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/python

# Given an integral number, determine if it's a square number:

import math
# python has a math function 

# def is_square(n):    
  #   isSquare = True
    # num1 = math.sqrt(n)
    # num2 = num1 ** 2
  #     if (num1 ** 2) == n:
  #         isSquare == True
  #     else: 
  #         isSquare == False
  #  return num2 # fix me

def is_square(n):
    result = False
    num = math.sqrt(n)
    num2 = num **2 
    if num2 == n and n > 1:
        result = True
    elif num2 != n or n < 1:
        result = False   

    return result

# reading on range https://www.w3schools.com/python/ref_func_range.asp

print(is_square(24))

print(is_square(9))
print(is_square(49)
)
print(is_square(6.7))
#print(is_square(-49))