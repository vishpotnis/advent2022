import sys
import re
import copy

class Monkey:

    lcm = 1

    def __init__(self, input_str):
        input_strs = input_str.split('\n')

        self.id = int(re.findall(r"\d+", input_strs[0])[0])
        self.items = [int(x) for x in re.findall(r"\d+", input_strs[1])]
        self.div_num = int(re.findall(r"\d+", input_strs[3])[0])
        self.div_true = int(re.findall(r"\d+", input_strs[4])[0])
        self.div_false = int(re.findall(r"\d+", input_strs[5])[0])

        if len(re.findall(r"\+", input_strs[2])) == 1:
            self.operation = 'ADD'
        else:
            self.operation = 'MULT'
        self.op_nums = [int(x) for x in re.findall(r"\d+", input_strs[2])]

        self.num_inspect = 0
        Monkey.lcm *= self.div_num

    def inspect_items(self, monkeys, reduce=False):
        for _ in range(len(self.items)):
            item_val = self.inspect()
            if reduce:
                item_val = item_val % Monkey.lcm
            else:
                item_val = item_val // 3
            target_monkey = self.test_item(item_val)

            monkeys[target_monkey].add_item(item_val)

    def inspect(self):
        self.num_inspect += 1

        val = self.items.pop(0)
        nums = [x for x in self.op_nums]
        while len(nums) != 2: nums.append(val)

        if self.operation == 'ADD':
            return nums[0] + nums[1]
        else:
            return nums[0] * nums[1]

    def test_item(self, item):
        if item % self.div_num == 0:
            return self.div_true
        else:
            return self.div_false

    def add_item(self, item):
        self.items.append(item)

    def print_items(self):
        print(f"Monkey {self.id}: {self.items}")


def main():
    input_fname = sys.argv[1]
    monkeys = read_input(input_fname)

    print(f"P1 Monkey Business: {monkey_rounds(copy.deepcopy(monkeys), 20, reduce=False)}")
    print(f"P2 Monkey Business: {monkey_rounds(copy.deepcopy(monkeys), 10000, reduce=True)}")
    

def monkey_rounds(monkeys, rounds, reduce):
    num_rounds = rounds
    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey.inspect_items(monkeys, reduce)

    num_inspect_arr = [monkey.num_inspect for monkey in monkeys]
    num_inspect_arr.sort(reverse=True)
    monkey_business = num_inspect_arr[0] * num_inspect_arr[1]
    return monkey_business    
    

def read_input(input_fname):
    with open(input_fname) as f:
        lines = f.read().split('\n\n')

    monkeys = [Monkey(line) for line in lines]       
    return monkeys


if __name__ == "__main__":
    main()