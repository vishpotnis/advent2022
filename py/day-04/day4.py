import sys

def main():
    
    if len(sys.argv) == 1:
        input_fname = "day4_input2.txt"
    else:
        input_fname = sys.argv[1]

    num_full_overlap = 0
    num_overlap = 0

    with open(input_fname) as f:
        for line in f:
            section = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in line.strip().split(',') ]
            if check_section_full_overlap(section):
                num_full_overlap += 1
            if check_section_overlap(section):
                num_overlap += 1

    print(f"Num full overlap sections: {num_full_overlap}")
    print(f"Num overlap sections: {num_overlap}")
   
def check_section_full_overlap(section):
    return section[0][0] >= section[1][0] and section[0][1] <= section[1][1] or  section[1][0] >= section[0][0] and section[1][1] <= section[0][1]

def check_section_overlap(section):
    return section[1][0] <= section[0][1] and section[1][1] >= section[0][0]



if __name__ == "__main__":
    main()