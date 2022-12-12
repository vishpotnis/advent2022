import sys


def main():
    
    input_fname = sys.argv[1]
    grid = read_input(input_fname)

    start_pos = get_pos(grid, 'S')[0]
    end_pos = get_pos(grid, 'E')[0]

    grid[start_pos[0]][start_pos[1]] = 'a'
    grid[end_pos[0]][end_pos[1]] = 'z'

    steps = BFS_search(grid, start_pos, end_pos, climb=True)
    print(f"P1 Total steps: {steps}")

    steps = BFS_search(grid, start_pos=end_pos, end_pos=None, climb=False)
    print(f"P2 Total steps: {steps}")


def BFS_search(grid, start_pos, end_pos, climb=True):

    q = [start_pos]
    steps = -1
    visited = set(start_pos)

    while len(q) != 0:
        size = len(q)
        steps += 1
        for _ in range(size):
            curr_pos = q.pop(0)
            if climb and curr_pos == end_pos:
                return steps
            elif not climb and grid[curr_pos[0]][curr_pos[1]] == 'a':
                return steps
            
            adj_pos_vec = get_adjacent(grid, curr_pos)
            for adj_pos in adj_pos_vec:
                if adj_pos not in visited:
                    if climb and ord(grid[adj_pos[0]][adj_pos[1]]) - ord(grid[curr_pos[0]][curr_pos[1]]) <= 1 or \
                       not climb and ord(grid[adj_pos[0]][adj_pos[1]]) - ord(grid[curr_pos[0]][curr_pos[1]]) >= -1:
                        visited.add(adj_pos)
                        q.append(adj_pos)


def get_adjacent(grid, pos):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    adj_pos = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if check_bounds(grid , (pos[0] + d[0], pos[1] + d[1]))]
    return adj_pos


def check_bounds(grid, pos):
    if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
        return False
    return True


def read_input(input_fname):
    with open(input_fname) as f:
        lines = f.read().splitlines()
    return [[c for c in line] for line in lines]

def get_pos(grid, val):
    return [(row,col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == val]


if __name__ == "__main__":
    main()