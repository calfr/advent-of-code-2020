from math import prod
def check_slope(slope_array,right_amount,down_amount):
    treeCount = 0
    x, y = 0, 0
    while y < len(slope_array):
        if slope_array[y][x] == "#":
            treeCount+=1
        x += right_amount
        x = x % len(slope_array[0])
        y += down_amount
    return treeCount

def parse_input(inputFilename):
    return [x.strip('\n') for x in open(inputFilename,"r").readlines()]

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    partA = check_slope(testInput,3,1)
    print(f"Part A:  Solution = {partA}")
    partB = prod([check_slope(testInput,1,1),check_slope(testInput,3,1),check_slope(testInput,5,1),check_slope(testInput,7,1),check_slope(testInput,1,2)])
    print(f"Part B:  Solution = {partB}")