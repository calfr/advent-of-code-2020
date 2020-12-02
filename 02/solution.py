from re import match

def check_password_v1(line):
    parsed_input = match("(\d+)-(\d+) ([a-z]): (.*)",line)
    minimum,maximum = int(parsed_input.group(1)), int(parsed_input.group(2))
    letter_to_count = parsed_input.group(3)
    input_string = parsed_input.group(4)
    return input_string.count(letter_to_count) <= maximum and input_string.count(letter_to_count) >= minimum

def check_password_v2(line):
    parsed_input = match("(\d+)-(\d+) ([a-z]): (.*)",line)
    pos1, pos2 = int(parsed_input.group(1)), int(parsed_input.group(2))
    letter_to_count = parsed_input.group(3)
    input_string = parsed_input.group(4)
    test1 = (input_string[pos1-1] == letter_to_count)
    test2 = (input_string[pos2-1] == letter_to_count)
    return (test1 or test2) and not (test1 and test2)

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = [x for x in open("input","r").readlines()]
    partA = sum([check_password_v1(line) for line in testInput])
    print(f"Part A:  Solution = {partA}")
    partB = sum([check_password_v2(line) for line in testInput])
    print(f"Part B:  Solution = {partB}")