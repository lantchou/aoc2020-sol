import re


def replace_and_write(result, i, val, mem):
    if i == len(result):
        addr = int(result, 2)
        mem[addr] = val
    elif result[i] == "X":
        # replace X at position i with 0 and recursively replace remaining X's in result
        new_result_0 = list(result)
        new_result_0[i] = "0"
        replace_and_write("".join(new_result_0), i + 1, val, mem)

        # replace X at position i with 1 and recursively replace remaining X's in result
        new_result_1 = list(result)
        new_result_1[i] = "1"
        replace_and_write("".join(new_result_1), i + 1, val, mem)
    else:
        replace_and_write(result, i + 1, val, mem)


with open("input.txt") as f:
    mask = ["0"] * 36  # 36 0-bits
    mem = dict()
    assn_pattern = re.compile(r"mem\[([0-9]+)\] = ([0-9]+)")  # pattern that matches address and value of mem assignment
    for instr in f:
        instr = instr.strip()
        if instr.startswith("mask"):
            mask = instr[7:]
        else:
            addr, val = assn_pattern.match(instr).groups()
            val = int(val)
            result = list('{:036b}'.format(int(addr)))
            for i, c in enumerate(mask):
                if c == "1":
                    result[i] = "1"
                elif c == "X":
                    result[i] = "X"

            replace_and_write("".join(result), 0, val, mem)

    mem_sum = 0
    for val in mem.values():
        mem_sum += val
    print(mem_sum)




