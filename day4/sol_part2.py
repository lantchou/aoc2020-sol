#!/usr/bin/python3

import re

with open("input.txt", "r") as f:
    req_fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    opt_fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"))

    valid_count = 0
    valid_vals = True
    seen_fields = set()
    
    lines = f.readlines()
    for i in range(len(lines) + 1):

        if i == len(lines) or len(lines[i].strip("\n")) == 0:
            if valid_vals and (seen_fields == req_fields or seen_fields == opt_fields):
                valid_count += 1
            seen_fields = set()
            valid_vals = True
        else:
            line = lines[i].strip("\n")
            line_fields = line.split(" ") 
            for field in line_fields:
                key = field[:3]
                val = field[4:]
                seen_fields.add(field[:3])
                if key == "byr":
                    val = int(val)
                    valid_vals = valid_vals and 1920 <= val <= 2002
                elif key == "iyr":
                    val = int(val)
                    valid_vals = valid_vals and 2010 <= val <= 2020 
                elif key == "eyr":
                    val = int(val)
                    valid_vals = valid_vals and 2020 <= val <= 2030
                elif key == "hgt":
                    pattern = re.compile(r"(\d+)(cm|in)")
                    match = pattern.match(val)
                    if bool(match):
                        size, meas = match.groups()
                        size = int(size)
                        valid_vals = valid_vals and ((meas == "cm" and 150 <= size <= 193) or (meas == "in" and 59 <= size <= 76))
                    else:
                        valid_vals = False
                elif key == "hcl":
                    pattern = re.compile(r"#([0-9]|[a-f]){6}$")
                    valid_vals = valid_vals and bool(pattern.match(val))
                elif key == "ecl":
                    pattern = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)$")
                    valid_vals = valid_vals and bool(pattern.match(val))
                elif key == "pid":
                    pattern = re.compile(r"\d{9}$")
                    valid_vals = valid_vals and bool(pattern.match(val))


        
    print(valid_count)

