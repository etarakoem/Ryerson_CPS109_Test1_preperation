# The following code examine three variables -- x, y, and z -- and prints the largest odd number among them.
# If none of them is odd, it prints a message to that effect.

def odd(string): # Aight I've created all possibilities, a test file to run the code
    list = string.split(',')
    x = int(list[0])
    y = int(list[1])
    z = int(list[2])
    print("Begin test: ----------------------------")
    print('Program result: ')
    # Custom program check here: Delete and copy paste to this to check
    if x % 2 == 1:
        if y % 2 == 1:
            if z % 2 == 1:
                print(max(x, y, z))
            else:
                print(max(x, y))
        elif z % 2 == 1:
            print(max(x, z))
        else:
            print(x)
    elif y % 2 == 1:
        if z % 2 == 0:
            print(max(y, z))
        else:
            print(z)
    elif z % 2 == 0:
        print(z)
    else:
        print('All three are even')
    # ==================================
    print("End of test program----------------------")
f = open('Odd test.txt','r')
for i in range(11):
    line = f.readline()
    odd(line)
    print("From sample test: ", line)
print("Note: if nothing in between 'begin test' and 'end of test', no result was printed")