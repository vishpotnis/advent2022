import sys


def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py/day-07/day7_input1.txt"
    else:
        input_fname = sys.argv[1]
    
    dir_sizes, root_size = read_input(input_fname)

    # Part 1
    size_sum = 0
    for dir_size in dir_sizes:
        if dir_size <= 100000:
            size_sum += dir_size
    print(f"Total size of all directories at most 100000: {size_sum}")

    # Part 2
    dir_sizes.sort()
    
    free_space = 70000000 - root_size
    needed_space = 30000000 - free_space
    print(f"Free Space: {free_space}")
    print(f"Need to delete: {needed_space}")

    for dir_size in dir_sizes:
        if dir_size > needed_space:
            print(f"Delete directory with size {dir_size} to make room")
            break


def read_input(input_fname):

    with open(input_fname) as f:
        lines = f.read().splitlines()

    dir_sizes = []
    stack = []    
    for line in lines:
        cmd = line.split()
        if cmd[0] == "$" and cmd[1] == "cd" and cmd[2] == "..":
            pop_stack_dir(stack, dir_sizes)
        elif cmd[0] == "$" and cmd[1] == "cd":
            stack.append('d')
        elif cmd[0] not in ("$", "dir"):
            stack.append(int(cmd[0]))
    
    while len(stack) > 1:
        pop_stack_dir(stack, dir_sizes)

    return dir_sizes, stack[0]


def pop_stack_dir(stack, dir_sizes):
    curr_size = 0
    while stack[-1] != 'd': curr_size += stack.pop()
    stack.pop()
    stack.append(curr_size)
    dir_sizes.append(curr_size)



if __name__ == "__main__":
    main()