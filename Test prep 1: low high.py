# Q1. Question 1 (5 points)
# An algorithm is a finite sequence of unambiguous instructions which will end in a finite number of steps.
# In Chapter 1, Guttag introduces an algorithm for finding the square root of a number.  The algorithm was presented by
# Heron of Alexandria almost a thousand years ago.  To find the square root of x, make a guess g.
# If g**2 is close enough to x, then report g as the square root.
# Otherwise, make a new guess which is the average of g and x/g.
#
# Check the new guess and keep repeating until the square of the guess is close enough to x.
# Suppose x is 99 and the first guess is 5.  Using this algorithm, how many guesses will it take until the guess squared is within 1 of x?  Use Python to answer this question.
def guess_count(x):
    g = 5
    epsilon = 1
    count = 1
    while abs(g**2-x) > epsilon:
        g = (g+x/g)/2
        count += 1
        a = abs(g ** 2 - x)
    return count

print(guess_count(99))

# Question about low - high but with 'y':
def guess_low_hi(x):
    epsilon = 0.01
    low = 0
    high = 100
    y = (low+high)/2
    count = 1
    while abs(y**4 - x) > epsilon:
        if y**4 > x:
            high = y
            y = (low+high)/2
            count += 1
        else:
            low = y
            y = (low+high)/2
            count += 1
    print(y,' ',count)
    return y
# guess_low_hi(100)

# Question with g = 50 started
def better_guess_fourth_root(k):
    epsilon = 0.01
    g = 50
    count = 1
    while abs(g**4-k) > epsilon:
        g = g - (g**4-k)/(4*g**3)
        count += 1
    print(g,' ',count)
    return g

# print(better_guess_fourth_root(100)**4)

