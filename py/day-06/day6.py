import sys


def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py\day-06\day6_input1.txt"
    else:
        input_fname = sys.argv[1]

    with open(input_fname) as f:
        buffer = f.readline().strip()

    print(f"Start of packet marker: {find_marker(buffer, num_unique=4)}")
    print(f"Start of message marker: {find_marker(buffer, num_unique=14)}")


def find_marker(buffer, num_unique):
    
    counts = [0] * 128

    for i in range(len(buffer)):
        if i >= num_unique:
            if any(count > 1 for count in counts):
                counts[ord(buffer[i-num_unique])] -= 1
            else:
                return i
        counts[ord(buffer[i])] += 1


if __name__ == "__main__":
    main()