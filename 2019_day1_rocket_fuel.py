"""
solution for Advent of Code 2019, Day 1 problem
https://adventofcode.com/2019/day/1

Reads a list of int and performs some basic math functions before summing.
Return an int
"""

from pathlib import Path

# notice the use of forward slash "/" even though its Windows. this is how Path works
FILENAME = "2019_day1_input.txt"

lineList = []
with open(FILENAME, "r") as f:
    # instead of f.readline() this lets us strip the newline(\n) char
    lineList = [int(line.rstrip("\n")) for line in f]

# per instructions: "take each mass, divide by 3, round down, subtract 2
print(sum((mass//3 - 2) for mass in lineList))


