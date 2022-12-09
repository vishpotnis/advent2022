import sys
from functools import reduce
import numpy as np


def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py\day-08\day8_input1.txt"
    else:
        input_fname = sys.argv[1]

    grid = read_input(input_fname)    
    find_trees(grid)

def read_input(input_fname):
    grid = []
    with open(input_fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        grid.append([int(c) for c in line])
    return np.array(grid)

def find_trees(grid):
    num_row = grid.shape[0]
    num_col = grid.shape[1]
    num_outer_trees = 2*num_row + 2*num_col - 4

    grid_t = grid.transpose()

    num_visible = 0
    score = 0

    for i in range(1, num_row - 1):
        for j in range(1, num_col - 1):
            visible_from_edge, visible_trees = get_visible_trees(grid, grid_t, (i,j))
            if visible_from_edge:
                num_visible += 1
            score = max(reduce(lambda x,y: x*y, [len(x) for x in visible_trees]), score)

    print(f"Total visible: {num_outer_trees + num_visible}")
    print(f"Best scenic score: {score}")



def get_visible_trees(grid, grid_t, tree_pos):

    tree_height = grid[tree_pos]
    visible_from_edge = False
    visible_trees = []

    dirs = {'R': grid[tree_pos[0], tree_pos[1]+1:],
            'L': grid[tree_pos[0], tree_pos[1]-1::-1],
            'D': grid_t[tree_pos[1], tree_pos[0]+1:],
            'U': grid_t[tree_pos[1], tree_pos[0]-1::-1]}

    for d in dirs.keys():
        x = dirs[d]
        if len(np.where(x>=tree_height)[0]):
            x = x[:np.where(x >= tree_height)[0][0]+1]
        else:
            visible_from_edge = True
        visible_trees.append(x)
    return visible_from_edge, visible_trees
    

if __name__ == "__main__":
    main()