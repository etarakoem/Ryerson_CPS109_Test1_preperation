# # Q.4
# def q4():
#     # result = 0
#     count = 0
#     for i in range(1,1001):
#         if (i%7 == 0) and (i%5!= 0):
#             count+= 1
#     print(count)
#     return
# q4()
#
# # Q.5
# def q5():
#     result = 0
#     for i in range(1,1001):
#         if (i%15 == 0) and (i%7!= 0):
#             result+= i
#     print(result)
#     return
# q5() # 28440
#
# Q.6
def guess_count_q6(x,g_first):
    g = g_first # First guess
    epsilon = 1 # As guess squared is within 1 of x
    count = 1 # First guess count
    print(f"Attempt {count} guess number: {g}")
    while abs(g**2-x) > epsilon:
        g = (g+x/g)/2
        count += 1
        print(f"Attempt {count} guess number: {g}")
    print(f"{g}**2 = {g**2}")
    print(count)

# guess_count_q6(99,5)
#
# # Q.7
# def productDigits(stringofdigits):
#     result = 1
#     for i in stringofdigits:
#         if i.isdigit():
#             result = int(i)*result
#     print(result)
#     return
#
# productDigits('ac')
# productDigits('abc123def5k') # 1235
# productDigits('098a765c432k112abc34567890') # 98765432 - got me there, "output as a number" haha
#
# Q.8
# import math as mt
# def guess_q8(x):
#     epsilon = 0.01
#     low = 0
#     high = x
#     y = (low+high)/2
#     count = 1
#     print(f"Guess attempt {count} as y = {y}")
#     while abs(y**6 - x) > epsilon:
#         if y**6 <= x:
#             low = y
#             y = (low+high)/2
#             count += 1
#             print(f"Guess attempt {count} as y = {y}")
#         else:
#             high = y
#             y = (low+high)/2
#             count += 1
#             print(f"Guess attempt {count} as y = {y}")
#     print(f"Final result: {y} at count no. {count}")
#     return y
# guess_q8(600)
#
# # Q.9
# def check(string):
#     list = []
#     mark = 1
#     for i in string:
#         list.append(string.count(i))
#     # print(list)
#     for i in range(len(list)-1):
#         if list[i] != list[i+1]:
#             mark = 0
#     if mark == 1:
#         return True
#     return False
# def perfectsquare(number):
#     for i in range(number):
#         if i*i == number:
#             return True
#     return False
# # Main program
# list = []
# for i in range(99,1000):
#     if perfectsquare(i) and check(str(i)):
#         list.append(i)
#
# print(list[0])
#
# # Q.10
# def perfectsquare(number):
#     for i in range(number):
#         if i*i == number:
#             return True
#     return False
# def perfectcube(number):
#     for i in range(number):
#         if i*i*i == number:
#             return True
#     return False
#
# list = []
# for i in range(2,10000):
#     if perfectsquare(i) and perfectcube(i):
#         list.append(i)
# print(list[0])
#
# Q.11
# def gen(n,k):
#     result = ""
#     for i in range(k):
#         result+= str(n+i)
#     return result
#
# def first(string):
#     count_test = []
#     potential_length = []
#     potential_string = []
#     potential_head = []
#     maximum = len(string)
#     for i in range(1, len(string)-1):
#         if string.count(string[:i]) != 1:
#             count_test.append(string.count(string[:i]))
#             potential_length.append(i+1)
#             potential_string.append((gen(int(string[:i+1]),int(maximum/(i+1)))))
#             potential_head.append(string[:i+1])
#     for i in range(len(potential_string)):
#         if potential_string[i] == string:
#             print("Found N is",potential_head[i])
#             return
#     print('No result')
#     return
# def run(x):
#     print("Decoding the smallest possible N from ")
#     print(x)
#     first(x)
#     print("----------------------------------------")
#     return
#
# sample = '193194195196197198199200201202203204'
# sample_1 = '12345678910111213141516171819'
# sample_2 = '142354142355142356142357142358142359142360142361142362142363142364142365'
# print("----------------------------------------")
# run(sample)
# run(sample_1)
# run(sample_2) # Check my result :)
