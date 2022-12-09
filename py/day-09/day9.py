import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

    def __iter__(self):
        yield self.x
        yield self.y

move_delta = {
    'U': (0, 1), 
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def main():
    if len(sys.argv) == 1:
        input_fname = r"py/day-09/day9_input3.txt"
    else:
        input_fname = sys.argv[1]

    with open(input_fname) as f:
        lines = f.read().splitlines()
    directions = [[line.split()[0], int(line.split()[1])] for line in lines]


    print(f"Number of unique tail coordinates for rope length 2: {len( get_unique_tail_coords(directions, rope_length=2))}")
    print(f"Number of unique tail coordinates for rope length 10: {len( get_unique_tail_coords(directions, rope_length=10))}")


def get_unique_tail_coords(directions, rope_length):

    unique_coord = set()
    rope = [Point(0,0) for _ in range(rope_length)]

    for direction in directions:
        for _ in range(direction[1]):
            rope[0].move(move_delta[direction[0]])

            for i in range(1, rope_length):
                if not is_point_adj(rope[i-1], rope[i]):
                    move_rope(rope[i-1], rope[i])

            unique_coord.add(tuple(rope[-1]))
    return unique_coord


def is_point_adj(head, tail):
    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1


def move_rope(head, tail):
    tail.x += (head.x > tail.x) - (head.x < tail.x)
    tail.y += (head.y > tail.y) - (head.y < tail.y)


if __name__ == "__main__":
    main()