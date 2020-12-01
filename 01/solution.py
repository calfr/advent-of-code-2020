from itertools import combinations
from math import prod

def sums_to_target(inputNumbers,target):
    return sum(inputNumbers) == target

def find_n_tuple_which_adds_to_target(numberSet,n,target):
    backlog = []
    for number in numberSet:
        for combination in combinations(backlog,n-1):
            if sum(combination)+number == target:
                return combination + (number,)
        backlog.append(number)
    return None


if __name__ == "__main__":
    print("Running against provided input...")
    testInput = [int(x) for x in open("input","r").readlines()]
    partA = find_n_tuple_which_adds_to_target(testInput,2,2020)
    print(f"Part A: Tuple = {partA}, Solution = {prod(partA)}")
    partB = find_n_tuple_which_adds_to_target(testInput,3,2020)
    print(f"Part B: Tuple = {partB}, Solution = {prod(partB)}")