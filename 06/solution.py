def parse_input(inputFilename):
    return [x for x in open(inputFilename,"r").read().split("\n\n")]

def get_answers_any(entry):
    answer_strings = entry.split("\n")
    answers = set([x for x in answer_strings[0]])
    for answer in answer_strings:
        answers = answers.union([x for x in answer])
    return answers

def get_answers_every(entry):
    answer_strings = entry.split("\n")
    answers = set([x for x in answer_strings[0]])
    for answer in answer_strings:
        answers = answers.intersection([x for x in answer])
    return answers


if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    anyAnswerCount = [len(get_answers_any(entry)) for entry in testInput]
    partA = sum(anyAnswerCount)
    print(f"Part A:  Solution = {partA}")
    everyAnswerCount = [len(get_answers_every(entry)) for entry in testInput]
    partB = sum(everyAnswerCount)
    print(f"Part B:  Solution = {partB}")