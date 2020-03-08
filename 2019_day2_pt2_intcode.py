'''
Advent of Code 2019, Day 2, Pt2

An encoding problem with list input of ints that's an analogy for
assembly language.

Intcode programs work in blocks of 4 numbers at a time, with 3 commands

1: tells you to take the numbers at the indices of the next two numbers,
add them, then place the result at the 3rd index

2: tells you to take the numbers at the indices of the next two numbers,
multiply them, then place the result at the 3rd index

99: tells you end of program

Pt2 asks you to find values for memory addresses 1 & 2 so that the value
at memory address 0 is 19690720
'''

FILENAME = "2019_day2_input.txt"

# both these file read implementations are overkill for a list of strictly numbers separated by commas
# but I was playing around with the different read methods

with open(FILENAME,"r") as f:
    codeList = []
    # reading in file line by line as list of strings. each string is split into a list
    for line in f:
        codeList.extend(line.strip("\n").replace(" ","").split(","))

codeList = [int(num) for num in codeList if num.isdigit()]


with open(FILENAME,"r") as f:
    codeList2 = []
    # using try/except because iterator will throw a StopIteration when it is done and next called
    try:
        while True:
            # next calls each line in file object that is split into list and iterated per element
            codeList2.extend(int(num) for num in next(f).strip("\n").replace(" ","").split(",") if num.isdigit())
    except:
        pass


# reads in file character by character and throws everything in a list

with open(FILENAME,"r") as f:
    codeList3 = []

    char = f.read(1)
    while char:
        codeList3.append(char)
        char = f.read(1)
        
def opCode(feed):  
    feed_copy = feed.copy()

    #!!!! When you do enumerate stepwise the index still only goes up by 1. You need to multiply by
    #your factor.

    for i,x in enumerate(feed_copy[::4]):
        
        # Operation 1: sum the numbers found at the next 2 locations put in location indexed by 4th
        if x == 1:
#            print(feed_copy[4*i+3],feed_copy[feed_copy[4*i+1]],"+",feed_copy[feed_copy[4*i+2]])
            feed_copy[feed_copy[4*i+3]] = feed_copy[feed_copy[4*i+1]] + feed_copy[feed_copy[4*i+2]]

        # Operation 2: multiply the numbers found at next 2 locations put in location indexed by 4th
        elif x == 2:
#            print(feed_copy[4*i+3],feed_copy[feed_copy[4*i+1]],"*",feed_copy[feed_copy[4*i+2]])
            feed_copy[feed_copy[4*i+3]] = feed_copy[feed_copy[4*i+1]] * feed_copy[feed_copy[4*i+2]]

        # Operation 99: end of program
        elif x == 99:
            break

        # other numbers meant something went wrong
        else:
            print("error in processing")
            break

    return feed_copy

def trial(feed):
    feed_copy = feed.copy()

    # trying some initial values to see how the system reacts.  linear? inverse?
    # because values at mem locations 1&2 are just added, order doesn't matter
    # both the values are integers beween 0 & 99, inclusive
    #
    # response seems to be linear somewhere below summed value of 160. let's try
    # with a bisector test approach
    
    # We want values at mem location 0 to be 19690720
    TARGET = 19690720

    # verification of opCode via known values test
    feed_copy[1] = 12
    feed_copy[2] = 2
    ret_copy = opCode(feed_copy)
    print("Value at memlocation 0 is 4138658:",ret_copy[0] == 4138658)

    next_input = (14,14,198)    
    while True:
        # calculated next suggested total input at memloc 1&2
        next_input = bisector(next_input[0],next_input[1],next_input[2], ret_copy[0], TARGET)
        feed_copy = feed.copy()
        feed_copy[1] = next_input[0] // 2
        feed_copy[2] = next_input[0] - feed_copy[1]
        print("New inputs:",feed_copy[1],feed_copy[2])
        ret_copy = opCode(feed_copy)
        print("1st:",feed_copy[1]," 2nd:",feed_copy[2]," 0th:", ret_copy[0])
        print(ret_copy[0] - TARGET)
        if abs(ret_copy[0] - TARGET) <= 20:
            break
    return

def brute_force(feed):
    feed_copy = feed.copy()

    # can't find a solution with bisector method (get a value within 8 though)
    # just going to number crunch instead
    TARGET = 19690720

    # verification of opCode via known values test
    feed_copy[1] = 12
    feed_copy[2] = 2
    ret_copy = opCode(feed_copy)
    print("Value at memlocation 0 is 4138658:",ret_copy[0] == 4138658)

    for i in range(100):
        for j in range(100):
            feed_copy = feed.copy()
            feed_copy[1] = i
            feed_copy[2] = j
            ret_copy = opCode(feed_copy)
            if ret_copy[0] == TARGET:
                print("Solution!  Found @ memcode1:",feed_copy[1]," and memcode2:",feed_copy[2])
    return
        

def bisector(prev_test, lower_bound, upper_bound, prev_result, targ_value):
    # this bisector test assumes linear response, especially since it'll weight
    # next test value accordingly
    #
    # input: all ints
    # output: int

    if prev_result < targ_value:
        lower_bound = max(prev_test,0)
    elif prev_result > targ_value:
        upper_bound = min(prev_test,198)

    new_test = int((upper_bound + lower_bound)/2)

    return (new_test,lower_bound, upper_bound)


        
