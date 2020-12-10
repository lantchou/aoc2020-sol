#!/usr/bin/python3

with open("input.txt") as f:

    instructions = f.read().splitlines()
    executed = set()
    acc = 0
    ip = 0

    while ip not in executed:
        curr_ins = instructions[ip]
        executed.add(ip)
        prefix = curr_ins[:3]
        if prefix == "acc" or prefix == "jmp":
            # acc or jmp instruction
            amount = int(curr_ins[5:])
            is_plus = curr_ins[4] == '+'
            if prefix == "acc":
                acc += amount if is_plus else -amount
                ip += 1
            else:
                ip += amount if is_plus else -amount
        else:
            # nop instruction
            ip += 1

    print(acc)