def parse_input(inputFilename):
    return [int(x.strip()) for x in open(inputFilename,"r").readlines()]

def check_if_composite(number,possibilities):
    for x in possibilities:
        if number - x in possibilities:
            return True
    return False

def find_first_xmas_error(buffer_size,inp):
    buffer = inp[:buffer_size]
    for item in inp[buffer_size:]:
        if not check_if_composite(item,buffer):
            return item
        else:
            buffer.pop(0)
            buffer.append(item)
    return False

def find_xmas_encryption_weakness(buffer_size,inp):
    weak_number = find_first_xmas_error(buffer_size,inp)
    setSize = 2
    while setSize < len(inp):
        for start in range(len(inp) - setSize):
            test = inp[start:start+setSize]
            if sum(test) == weak_number:
                return min(test) + max(test)
        setSize += 1
    return False

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    partA = find_first_xmas_error(25,testInput)
    print(f"Part A:  Solution = {partA}")
    partB = find_xmas_encryption_weakness(25,testInput)
    print(f"Part B:  Solution = {partB}")