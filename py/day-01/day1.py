
def main():

    input_fname = "day1_input1.txt"
    max_calories = get_max_calories(input_fname)
    print(f"Max calories {max_calories}")

    top_calories = get_top3_calories(input_fname)
    print(f"Top 3 calories:")
    for i in range(len(top_calories)):
        print(f"{i+1}: {top_calories[i]}")
    print(f"Sum {sum(top_calories)}")
    


# Part 1
def get_max_calories(input_fname):

    max_calories = 0
    current_calories = 0

    with open(input_fname) as f:
        for line in f:
            if line == "\n":                
                max_calories = max(max_calories, current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
    
    return max_calories

# Part 2
def get_top3_calories(input_fname):

    top_calories = []
    current_calories = 0

    with open(input_fname) as f:
        for line in f:
            if line == "\n":
                top_calories.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)

    top_calories.sort(reverse=True) 
    return top_calories[0:3]


if __name__ == "__main__":
    main()