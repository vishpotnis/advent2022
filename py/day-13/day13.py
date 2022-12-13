import sys
import ast
from functools import cmp_to_key

def main():
    
    input_fname = sys.argv[1]

    packets = read_input(input_fname)
    order_idx = [i//2 + 1 for i in range(0, len(packets), 2) if compare_packets(packets[i], packets[i+1])]
    print(f"P1 Index sum: {sum(order_idx)}")

    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(compare_func))

    decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(f"P2 Decoder key: {decoder_key}")


def read_input(input_fname):
    with open(input_fname) as f:
        return [ast.literal_eval(line) for line in f if line != "\n"]

def compare_func(pkt1, pkt2):
    if compare_packets(pkt1, pkt2): return -1
    elif not compare_packets(pkt1, pkt2): return 1
    else: return 0

def compare_packets(pkt1, pkt2):

    for i in range(min(len(pkt1), len(pkt2))):
        res = None
        if type(pkt1[i]) == int and type(pkt2[i]) == int:
            if pkt1[i] < pkt2[i]: return True
            elif pkt1[i] > pkt2[i]: return False
        elif type(pkt1[i]) == list and type(pkt2[i]) == list:
            res = compare_packets(pkt1[i], pkt2[i])
        elif type(pkt1[i]) == int:
            res = compare_packets([pkt1[i]], pkt2[i])            
        elif type(pkt2[i]) == int:
            res = compare_packets(pkt1[i], [pkt2[i]])
        if res is not None: return res

    if len(pkt1) != len(pkt2):
        return len(pkt1) < len(pkt2)


if __name__ == "__main__":
    main()