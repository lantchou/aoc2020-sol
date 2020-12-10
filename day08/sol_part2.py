#!/usr/bin/python3

with open("input.txt") as f:

    instructions = f.read().splitlines()
    acc = 0
    ip = 0
    executed = set()
    terminated = False
    to_switch = 0

    while not terminated:

        # switch nop and jmp
        replaced = "nop" if instructions[to_switch][:3] == "nop" else "jmp"
        instructions[to_switch] = instructions[to_switch].replace("nop", "jmp") \
            if replaced == "nop" else instructions[to_switch].replace("jmp", "nop")

        acc = 0
        ip = 0
        executed = set()

        while ip not in executed and 0 <= ip < len(instructions):

            executed.add(ip)

            curr_ins = instructions[ip]
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

        # switch back jmp and nop
        instructions[to_switch] = instructions[to_switch].replace("jmp", "nop")\
            if replaced == "nop" else instructions[to_switch].replace("nop", "jmp")

        # increment next to switch
        to_switch += 1

        terminated = ip == len(instructions)

    print(acc)
