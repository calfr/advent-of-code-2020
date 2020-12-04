from re import match

def parse_input(inputFilename):
    return [x for x in open(inputFilename,"r").read().split("\n\n")]

def parse_passport(passportString):
    passport = {}
    # k:v pairs, split by newlines and spaces.
    for line in passportString.split("\n"):
        for entry in line.split(" "):
            kv = entry.split(":")
            passport[kv[0]] = kv[1]
    return passport

def check_presence(passportDict):
    return all([x in passportDict.keys() for x in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]])

def check_validity(passportDict):
    tests = [
        validateRangeInclusive(passportDict["byr"],1920,2002),
        validateRangeInclusive(passportDict["iyr"],2010,2020),
        validateRangeInclusive(passportDict["eyr"],2020,2030),
        validateHeightRange(passportDict["hgt"],cmmin=150,cmmax=193,inmin=59,inmax=76),
        validateRegex(passportDict["hcl"],"^#[0-9a-f]{6}$"),
        validateOptions(passportDict["ecl"],["amb","blu","brn","gry","grn","hzl","oth"]),
        validateRegex(passportDict["pid"],"^[0-9]{9}$")
    ]
    return all(tests)

def check_presence_and_validity(passportDict):
    result = check_presence(passportDict) and check_validity(passportDict)
    return result

def validateRangeInclusive(value,mini,maxi):
    return int(value) >= mini and int(value) <= maxi

def validateHeightRange(height,cmmin,cmmax,inmin,inmax):
    if height.endswith("cm"):
        return validateRangeInclusive(height[:-2],cmmin,cmmax)
    elif height.endswith("in"):
        return validateRangeInclusive(height[:-2],inmin,inmax)
    else:
        return False

def validateRegex(value,expression):
    return match(expression,value)

def validateOptions(value,options):
    return value in options

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    partA = sum([check_presence(parse_passport(entry)) for entry in testInput])
    print(f"Part A:  Solution = {partA}")
    partB = sum([check_presence_and_validity(parse_passport(entry)) for entry in testInput])
    print(f"Part B:  Solution = {partB}")