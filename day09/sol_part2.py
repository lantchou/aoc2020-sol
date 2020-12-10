#!/usr/bin/python3

from sol_part1 import find_weakness


if __name__ == "__main__":

    with open("input.txt", "r") as f:

        numbers = [int(line.strip("\n")) for line in f]
        weakness = find_weakness(numbers)

        for start in range(len(numbers)):
            for end in range(start + 1, len(numbers)):
                sublist = numbers[start:end + 1]
                if sum(sublist) == weakness:
                    print(min(sublist) + max(sublist))
                    break
