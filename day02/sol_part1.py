#!/usr/bin/python3

import re

with open("input.txt", "r") as f:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    valid_count = 0
    for line in f:
        line = line.strip("\n")
        min_freq, max_freq, c, s = pattern.match(line).groups()
        freq = s.count(c) 
        if int(min_freq) <= freq <= int(max_freq):
            valid_count += 1

print(valid_count)

