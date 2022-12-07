import sys

class Node:

    def __init__(self, name, parent, is_dir, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.is_dir = is_dir
        self.size = size

    def add_child(self, node):
        self.children.append(node)

    def find_child(self, name):
        for node in self.children:
            if node.name == name:
                return node
        return None

    def __str__(self):
        string = f"name: {self.name}\n"
        string += f"children: {self.children}\n"
        string += f"size: {self.size}\n"
        string += f"is_dir: {self.is_dir}\n"
        return string

def calc_size(node):
    calc_size_helper(node) 

def calc_size_helper(node):
    if not node.is_dir:
        return node.size

    size = 0
    for child in node.children:
        size += calc_size_helper(child)

    node.size = size
    return size


def get_dir_sizes(node, dir_sizes):
    if node.is_dir:
        dir_sizes.append(node.size)
    for child in node.children:
        get_dir_sizes(child, dir_sizes)

def print_dir_tree(node, level=0):
    string = '  '*level
    string += f'- {node.name}'
    if node.is_dir:
        string += f' (dir, size={node.size})'
    else:
        string += f' (file, size={node.size})'
    print(string)
    for child in node.children:
        print_dir_tree(child, level+1)


def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py\day-07\day7_input2.txt"
    else:
        input_fname = sys.argv[1]

    root = read_input(input_fname)
    calc_size(root)

    print_dir_tree(root)

    dir_sizes = []
    get_dir_sizes(root, dir_sizes)

    # Part 1
    size_sum = 0
    for dir_size in dir_sizes:
        if dir_size <= 100000:
            size_sum += dir_size
    print(f"Total size of all directories at most 100000: {size_sum}")

    # Part 2
    dir_sizes.sort()
    
    free_space = 70000000 - root.size
    needed_space = 30000000 - free_space
    print(f"Free Space: {free_space}")
    print(f"Need to delete: {needed_space}")

    for dir_size in dir_sizes:
        if dir_size > needed_space:
            print(f"Delete directory with size {dir_size} to make room")
            break


def read_input(input_fname):

    root = Node('/', None, is_dir=True)
    curr_node = root

    with open(input_fname) as f:
        lines = f.read().splitlines()
    
    i = 1
    while i < len(lines):
        if lines[i][0] == '$':
            cmd = lines[i].split()
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    curr_node = curr_node.parent
                else:
                    curr_node = curr_node.find_child(cmd[2])
            elif cmd[1] == 'ls':
                # create children for current node
                while i+1 < len(lines) and lines[i+1][0] != '$':
                    ls_out = lines[i+1].split()
                    if ls_out[0] == 'dir':
                        tmp_node = Node(ls_out[1], curr_node, is_dir=True, size=0)
                    else:
                        tmp_node = Node(ls_out[1], curr_node, is_dir=False, size=int(ls_out[0]))
                    curr_node.add_child(tmp_node)
                    i += 1

        i += 1
    
    return root
    

if __name__ == "__main__":
    main()