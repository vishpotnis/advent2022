
import sys


def main():
    
    if len(sys.argv) == 1:
        input_fname = "day2_input2.txt"
    else:
        input_fname = sys.argv[1]

    part1(input_fname)
    part2(input_fname)


def part1(input_fname):

    outcomes = {
        "A X" : 1 + 3,
        "A Y" : 2 + 6,
        "A Z" : 3 + 0,
        "B X" : 1 + 0,
        "B Y" : 2 + 3,
        "B Z" : 3 + 6,
        "C X" : 1 + 6,
        "C Y" : 2 + 0, 
        "C Z" : 3 + 3,
    }

    score = 0
    with open(input_fname) as f:
        for line in f:
            score += outcomes[line.strip()]

    print(f"P1 Score: {score}")

def part2(input_fname):

    outcomes = {
        "A X" : 0 + 3,
        "A Y" : 3 + 1,
        "A Z" : 6 + 2,
        "B X" : 0 + 1,
        "B Y" : 3 + 2,
        "B Z" : 6 + 3,
        "C X" : 0 + 2,
        "C Y" : 3 + 3, 
        "C Z" : 6 + 1,
    }

    score = 0
    with open(input_fname) as f:
        for line in f:
            score += outcomes[line.strip()]

    print(f"P2 Score: {score}")




if __name__ == "__main__":
    main()