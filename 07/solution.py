from re import match
def parse_input(inputFilename):
    return [x.strip() for x in open(inputFilename,"r").readlines()]

def parse_instructions(input_array):
    instructions = {}
    for item in input_array:
        colour,contents = parse_instruction(item)
        instructions[colour] = contents
    return instructions

def parse_instruction(input_string):
    matches = match("(.*) bags contain (.*)\.",input_string)
    bag_colour,contents_string = matches.group(1),matches.group(2)
    contents = {}
    for content in contents_string.split(", "):
        content = content.strip()
        second_matches = match("([0-9]+) (.*) bags?(?:,|.)?",content)
        if second_matches:
            contents[second_matches.group(2)] = second_matches.group(1)
    return (bag_colour,contents)

def find_compatible_bags(bag_colour,instruction_dict):
    compatible_bags = set()
    for k,v in instruction_dict.items():
        if bag_colour in v.keys():
            compatible_bags.add(k)
            compatible_bags = compatible_bags.union(find_compatible_bags(k,instruction_dict))
    return compatible_bags

def get_bag_mass(bag_colour,instruction_dict):
    count = 1
    if instruction_dict.get(bag_colour):
        k,v = bag_colour,instruction_dict[bag_colour]
        print(k,v)
        for colour, amount in v.items():
            count += get_bag_mass(colour,instruction_dict) * int(amount)
    return count

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    partA = find_compatible_bags("shiny gold",parse_instructions(testInput))
    print(f"Part A:  Solution = {len(partA)}")
    partB = get_bag_mass("shiny gold",parse_instructions(testInput))
    print(f"Part B:  Solution = {partB-1}") # Subtract 1 because we're not counting the initial bag!