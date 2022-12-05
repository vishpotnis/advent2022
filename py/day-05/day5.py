import sys
import re
import copy

def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py\day-05\day5_input1.txt"
    else:
        input_fname = sys.argv[1]

    stacks, instructions = read_input(input_fname)

    print(get_top_stack_string(follow_instructions(copy.deepcopy(stacks), instructions, move_multiple=False)))
    print(get_top_stack_string(follow_instructions(copy.deepcopy(stacks), instructions, move_multiple=True)))


def get_top_stack_string(stacks):
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result

def follow_instructions(stacks, instructions, move_multiple=False):

    for instruction in instructions:
        nums = re.findall(r"\d+", instruction)
        num_move = int(nums[0])
        source_stack = int(nums[1]) - 1
        target_stack = int(nums[2]) - 1

        if move_multiple:
            stacks[target_stack] = stacks[target_stack] + stacks[source_stack][-num_move:]
            del(stacks[source_stack][-num_move:])
        else:
            for _ in range(num_move):
                stacks[target_stack].append(stacks[source_stack].pop())

    return stacks


def get_stacks_from_input(lines):
   
    num_stacks = int(lines.pop().strip()[-1])
    stacks = [[] for _ in range(num_stacks)]

    while lines:
        line = lines.pop()
        for col in range(num_stacks):
            if line[col*4+1] != ' ':
                stacks[col].append(line[col*4+1])

    return stacks


def read_input(input_fname):

    with open(input_fname) as f:
        lines = f.readlines()

    stacks_input = []
    index = 0
    while(lines[index] != "\n"): 
        stacks_input.append(lines[index])
        index += 1

    stacks = get_stacks_from_input(stacks_input)
    instructions = lines[index+1:]

    return stacks, instructions


if __name__ == "__main__":
    main()