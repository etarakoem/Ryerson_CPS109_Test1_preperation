# Q.5 Write a program sumDigits(stringofdigits) to add the digits from a string, where all of the letters are digits.
# For example, sumDigits('123') prints 6, since 1 + 2 + 3 is 6.
# What is sumDigits('09876543211234567890')?
# Your answer should be a number.
# The function int() should help.
# Your function should be written in the file test1.py.

def sumDigits(stringofdigits):
    result = 0
    for i in stringofdigits:
        result += int(i)
    return result

# print("SumDigits: ",sumDigits('09876543211234567890'))

# Q.6 Use exhaustive enumeration to find all the numbers from 1 to 1000, inclusive, that are divisible by 7 but not by 5.
# The sum of those numbers is:
def look_in_range(start,stop):
    list = []
    for i in range(start,stop):
        if (i%7 == 0) and (i%5 != 0):
            list.append(i)
    return sum(list)
# print("Sum in range 1,1000: ")
print(look_in_range(1,1000))

# Q.9
# Note that the Python built in function bin(n) converts a decimal
# number n to binary, and int(b, 2) converts a string representation of
# a binary number to a decimal number. For example bin(3) is '0b11',
# and int('11', 2) is the same as int('0b11', 2) which is 3. You can
# use either of these functions to answer this question.
#
# Write a Python program to find the sum of the binary numbers
# in list L, where the binary numbers do not have the quote marks
# necessary for the int() function. For example, if
# L = [101, 11, 1010]
# then the sum is 5 + 3 + 10 = 18.
#
# What is the sum when L is
# L = [10100, 101000, 100000, 1011111, 1000, 1010111, 1010010, 11001, 101100, 10111, 11011, 1011010, 11101, 10, 110011,
# 1001111, 110010, 101100, 100001, 111001]
#
# Question 9 options:
def sumbinary(a):
    result = 0
    for i in a:
        result += int(str(i),2)
    return result
L = [10100, 101000, 100000, 1011111, 1000, 1010111, 1010010, 11001, 101100, 10111, 11011, 1011010, 11101, 10, 110011, 1001111, 110010, 101100, 100001, 111001]
print('Sum of L is: ',sumbinary(L))

# Q.10
# Write a Python program that finds S = the sum of all the integers from 1 to N inclusive that evenly divide into N = 4312943
# For example, if N = 10, then the sum S = 1 + 2 + 5 + 10 = 18
# The value of S is:
def q10(number):
    result = 0
    for i in range(1,number+1):
        if number%i == 0:
            result += i
    print(result)
q10(4312943)
