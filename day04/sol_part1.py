#!/usr/bin/python3

with open("input.txt", "r") as f:
    req_fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    opt_fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"))

    valid_count = 0
    seen_fields = set()
    
    i = 0
    lines = f.readlines()
    for i in range(len(lines) + 1):

        if i == len(lines) or len(lines[i].strip("\n")) == 0:
            if sorted(seen_fields) == sorted(req_fields) or sorted(seen_fields) == sorted(opt_fields):
                valid_count += 1
            seen_fields = set()
        else:
            line = lines[i].strip("\n")
            line_fields = line.split(" ") 
            for field in line_fields:
                seen_fields.add(field[:3])
        
    print(valid_count)

