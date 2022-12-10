import sys


def main():
    
    if len(sys.argv) == 1:
        input_fname = r"py\day-10\day10_input1.txt"
    else:
        input_fname = sys.argv[1]

    lines = read_input(input_fname)
    state = process_instructions(lines)
    print(f"Signal Strength: {get_signal_strength(state)}")
    draw_crt(state)


def read_input(input_fname):
    with open(input_fname) as f:
        lines = f.read().splitlines()
    return lines

def process_instructions(lines):
    state = []
    reg_x = 1
    for line in lines:
        instruction = line.split()
        if instruction[0] == 'noop':
            state += [[reg_x, reg_x]]
        elif instruction[0] == 'addx':
            state += [[reg_x, reg_x]]
            state += [[reg_x, reg_x + int(instruction[1])]]
            reg_x += int(instruction[1])
    return state

def get_signal_strength(state):
    signal_strength = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for cycle in cycles:
        signal_strength += state[cycle-1][0] * cycle
    return signal_strength

def draw_crt(state):
    crt_str = ""
    for i in range(len(state)):
        scan_pos = i % 40
        sprite_pos = [state[i][0]-1, state[i][0], state[i][0]+1]
        crt_str += "#" if scan_pos in sprite_pos else "."

    for i in range(6):
        print(crt_str[(i)*40:(i+1)*40])




if __name__ == "__main__":
    main()