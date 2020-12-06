#!/usr/bin/python3

with open("input.txt", "r") as f:

    lines = f.read().splitlines()
    n_lines = len(lines)

    yes_count = 0
    answ = set()

    for i in range(n_lines + 1):
        if i == n_lines or len(lines[i]) == 0:
            yes_count += len(answ)
            answ = set()
        else:
            line = lines[i]
            answ = answ.union(set([c for c in line]))

    print(yes_count)

