"""
solution for Advent of Code 2019, Day 1 problem
https://adventofcode.com/2019/day/1

Reads a list of int and performs some basic math functions before summing.
Return an int that is the weight of fuel only
"""

from pathlib import Path

# notice the use of forward slash "/" even though its Windows. this is how Path works
FILENAME = Path("C:/Users/BrianC/Desktop/Coding Sandbox/AdventOfCode/2019_day1_input.txt")

lineList = []
with open(FILENAME, "r") as f:
    # instead of f.readline() this lets us strip the newline(\n) char
    lineList = [int(line.rstrip("\n")) for line in f]

# per instructions: "take each mass, divide by 3, round down, subtract 2

# per Part 2, now need to consider fuel for weight of fuel, until zero/neg
# but calculated per module, rather than the total sum

def fuelCalc(mass):
    fuel_weight = 0
    func = lambda x: x//3 - 2
    new_fuel = func(mass)

    while new_fuel > 0:
        fuel_weight += new_fuel
        new_fuel = func(new_fuel)

    return fuel_weight

fuel_for_fuel = list(map(fuelCalc, lineList))

print(lineList[0:10], fuel_for_fuel[0:10])
# just want weight of fuel, not fuel and modules
print(sum(fuel_for_fuel))
