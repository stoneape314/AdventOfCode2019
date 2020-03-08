'''
Advent of Code 2019, Day 2

An encoding problem with list input of ints that's an analogy for
assembly language.

Intcode programs work in blocks of 4 numbers at a time, with 3 commands

1: tells you to take the numbers at the indices of the next two numbers,
add them, then place the result at the 3rd index

2: tells you to take the numbers at the indices of the next two numbers,
multiply them, then place the result at the 3rd index

99: tells you end of program
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
            print(feed_copy[4*i+3],feed_copy[feed_copy[4*i+1]],"+",feed_copy[feed_copy[4*i+2]])
            feed_copy[feed_copy[4*i+3]] = feed_copy[feed_copy[4*i+1]] + feed_copy[feed_copy[4*i+2]]

        # Operation 2: multiply the numbers found at next 2 locations put in location indexed by 4th
        elif x == 2:
            print(feed_copy[4*i+3],feed_copy[feed_copy[4*i+1]],"*",feed_copy[feed_copy[4*i+2]])
            feed_copy[feed_copy[4*i+3]] = feed_copy[feed_copy[4*i+1]] * feed_copy[feed_copy[4*i+2]]

        # Operation 99: end of program
        elif x == 99:
            break

        # other numbers meant something went wrong
        else:
            print("error in processing")
            break

    return feed_copy




    
    
