#!/usr/bin/python3

with open("input.txt", "r") as f:

    lines = f.read().splitlines()
    n_lines = len(lines)

    yes_count = 0
    group_size = 0
    answ = dict()

    for i in range(n_lines + 1):
        if i == n_lines or len(lines[i]) == 0:
            yes_count += sum([1 for k in answ if answ[k] == group_size])
            group_size = 0
            answ = dict()
        else:
            line = lines[i]
            qs = set([c for c in line])
            for q in qs:
                if q in answ:
                    answ[q] += 1
                else:
                    answ[q] = 1
            group_size += 1

    print(yes_count)

