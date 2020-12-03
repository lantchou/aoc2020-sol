#!/usr/bin/python3

with open("input.txt", "r") as f:
    numbers = f.read().splitlines()
    
    for i in range(len(numbers)):
        n1 = int(numbers[i])
        for j in range(i + 1, len(numbers)):
            n2 = int(numbers[j])
            if n1 + n2 == 2020:
                print(n1 * n2)
                break

