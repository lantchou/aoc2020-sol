#!/usr/bin/python3

import re

with open("input.txt", "r") as f:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    valid_count = 0
    for line in f:
        line = line.strip("\n")
        pos1, pos2, c, s = pattern.match(line).groups()
        pos1 = int(pos1)
        pos2 = int(pos2)
        if (s[pos1-1] == c) != (s[pos2-1] == c):  # fancy way to xor two bools
            valid_count += 1

print(valid_count)

