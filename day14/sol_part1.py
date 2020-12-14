import re


with open("input.txt") as f:
    mask_ones = 0x000000000  # 36 0-bits
    mask_zeros = 0xFFFFFFFFF  # 36 1-bits
    mem = dict()
    assn_pattern = re.compile(r"mem\[([0-9]+)\] = ([0-9]+)")  # pattern that matches address and value of mem assignment
    for instr in f:
        instr = instr.strip()
        if instr.startswith("mask"):
            mask_val = instr[7:]
            mask_ones = int(mask_val.replace("X", "0"), 2)
            mask_zeros = int(mask_val.replace("X", "1"), 2)
        else:
            addr, val = assn_pattern.match(instr).groups()
            addr = int(addr)
            val = int(val)
            val |= mask_ones
            val &= mask_zeros
            mem[addr] = val

    mem_sum = 0
    for val in mem.values():
        mem_sum += val
    print(mem_sum)




