import sys


def main():
    
    input_fname = sys.argv[1]
    rock_pos, y_max = read_input(input_fname)

    # Part 1
    sand_pos = {}
    num_sand = 0
    while(drop_sand(rock_pos, sand_pos, y_max)): num_sand += 1
    print(f"P1 Num sand: {num_sand}")

    # Part 2
    sand_pos = {}   
    floor = y_max + 2
    for x_val in range(-10000, 10000, 1): rock_pos[(x_val, floor)] = '#'

    num_sand = 0
    while(drop_sand(rock_pos, sand_pos, y_max, True)): num_sand += 1
    print(f"P2 Num sand: {num_sand + 1}")


def drop_sand(rock_pos, sand_pos, y_max, floor=False):

    curr_sand_pos = (500, 0)
    falling = True
    while(falling):
        if not floor and curr_sand_pos[1] >= y_max: return False

        if check_pos(rock_pos, sand_pos, (curr_sand_pos[0], curr_sand_pos[1] + 1)):
            curr_sand_pos = (curr_sand_pos[0], curr_sand_pos[1] + 1)
        elif check_pos(rock_pos, sand_pos, (curr_sand_pos[0] - 1, curr_sand_pos[1] + 1)):
            curr_sand_pos = (curr_sand_pos[0] - 1, curr_sand_pos[1] + 1)
        elif check_pos(rock_pos, sand_pos, (curr_sand_pos[0] + 1, curr_sand_pos[1] + 1)):
            curr_sand_pos = (curr_sand_pos[0] + 1, curr_sand_pos[1] + 1)
        else:
            falling = False
    if curr_sand_pos == (500, 0):
        return False
    sand_pos[curr_sand_pos] = 'o'
    return True

def check_pos(rock_pos, sand_pos, pos):
    if pos in rock_pos or pos in sand_pos:
        return False
    return True

def read_input(input_fname):

    rock_pos = {}
    y_max = 0
    with open(input_fname) as f:
        lines = f.readlines()
    for line in lines:
        coords = line.strip().split(' -> ')

        for i in range(len(coords) - 1):
            start = [int(x) for x in coords[i].split(',')]
            end = [int(x) for x in coords[i+1].split(',')]
            y_max = max(y_max, start[1], end[1])

            if start[0] == end[0]:
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    rock_pos[(start[0], y)] = '#'
            elif start[1] == end[1]:
                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    rock_pos[(x, start[1])] = '#'

    return rock_pos, y_max


def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    main()