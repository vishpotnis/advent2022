import sys

def main():
    
    if len(sys.argv) == 1:
        input_fname = "day2_input2.txt"
    else:
        input_fname = sys.argv[1]

    part1_incorrect_item(input_fname)
    part2_get_badge(input_fname)
   


def part1_incorrect_item(fname):

    with open(fname) as f:
        priority_sum = 0
        for line in f:
            priority_sum += get_priority(get_incorrect_item(line))
    
    print(f"Incorrect item priority sum: {priority_sum}")

def part2_get_badge(fname):

    with open(fname) as f:
        lines = [line.strip() for line in f]

    priority_sum = 0
    for i in range(0, len(lines), 3):
        badge = identify_badge(lines[i:i+3])
        priority_sum += get_priority(badge)
    
    print(f"Find badge priority sum: {priority_sum}")

def identify_badge(lines):
    group1 = get_bitfield(lines[0])
    group2 = get_bitfield(lines[1])
    group3 = get_bitfield(lines[2])

    for i, (x, y, z) in enumerate(zip(group1, group2, group3)):
        if x & y & z: return chr(i)
    

def get_incorrect_item(line):    
    first_bucket = get_bitfield(line[:len(line)//2])
    second_bucket = get_bitfield(line[len(line)//2:])

    for i, (x, y) in enumerate(zip(first_bucket, second_bucket)):
        if x & y: return chr(i)

def get_bitfield(line):
    bitfield = [0] * 128
    for c in line:
        bitfield[ord(c)] |= 1
    return bitfield

def get_priority(char):
    if char >= 'a' and char <= 'z':
        return ord(char) - ord('a') + 1
    elif char >= 'A' and char <= 'Z':
        return ord(char) - ord('A') + 27
        
    
            


if __name__ == "__main__":
    main()