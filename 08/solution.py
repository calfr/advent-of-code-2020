def parse_input(inputFilename):
    return [x.strip() for x in open(inputFilename,"r").readlines()]

def run_instruction(instruction,acc,pos):
    if instruction[:3] == "acc":
        acc += int(instruction[4:])
        pos += 1
    elif instruction[:3] == "jmp":
        pos += int(instruction[4:])
    elif instruction[:3] == "nop":
        pos += 1
    return acc,pos

def run_program_until_repeat(program):
    acc = 0
    pos = 0
    stopped = False
    visited = set()
    while pos not in visited:
        if pos >= len(program):
            if pos == len(program):
                stopped = True
                break
            else:
                break
        visited.add(pos)
        acc,pos = run_instruction(program[pos],acc,pos)
    return acc,stopped

def attempt_toggle_bruteforce(program):
    for pos in range(len(program)):
        if program[pos][:3] in ["jmp","nop"]:
            patched_program = program.copy()
            if program[pos][:3] == "jmp":
                patched_program[pos] = "nop" + patched_program[pos][3:]
            elif program[pos][:3] == "nop":
                patched_program[pos] = "jmp" + patched_program[pos][3:]
            a,b = run_program_until_repeat(patched_program)
            if b:
                return a
    return False

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    partA = run_program_until_repeat(testInput)[0]
    print(f"Part A:  Solution = {partA}")
    partB = attempt_toggle_bruteforce(testInput)
    print(f"Part B:  Solution = {partB}")