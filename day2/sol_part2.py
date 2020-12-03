#!/usr/bin/python3

import re

with open("input.txt", "r") as f:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    valid_count = 0
    for line in f:
        line = line.strip("\n")
        req_pos, proh_pos, c, s = pattern.match(line).groups()
        req_pos = int(req_pos)
        proh_pos = int(proh_pos)
        if (s[req_pos-1] == c) != (s[proh_pos-1] == c):  # fancy way to xor two bools
            valid_count += 1

print(valid_count)

