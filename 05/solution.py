def parse_input(inputFilename):
    return [x.strip() for x in open(inputFilename,"r").readlines()]

def get_seat_row(boarding_pass):
    return int(boarding_pass[:7].replace("F","0").replace("B","1"),2)

def get_seat_number(boarding_pass):
    return int(boarding_pass[-3:].replace("L","0").replace("R","1"),2)

def get_seat_id(boarding_pass):
    print(boarding_pass,get_seat_row(boarding_pass),get_seat_number(boarding_pass))
    return (get_seat_row(boarding_pass) * 8) + (get_seat_number(boarding_pass))

if __name__ == "__main__":
    print("Running against provided input...")
    testInput = parse_input("input")
    seatsTaken = [get_seat_id(entry) for entry in testInput]
    partA = max(seatsTaken)
    print(f"Part A:  Solution = {partA}")
    partB = [x for x in range(min(seatsTaken),max(seatsTaken)) if x not in seatsTaken and x+1 in seatsTaken and x-1 in seatsTaken]
    print(f"Part B:  Solution = {partB}")