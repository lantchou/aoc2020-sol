#!/usr/bin/python3

with open("input.txt", "r") as f:
    numbers = f.read().splitlines()
    
    for i in range(len(numbers)):
        n1 = int(numbers[i])
        for j in range(i + 1, len(numbers)):
            n2 = int(numbers[j])
            for k in range(j + 1, len(numbers)):
                n3 = int(numbers[k])

                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)
                    break

