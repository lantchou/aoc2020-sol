#!/usr/bin/python3

def find_weakness(numbers):
    i = 25
    all_have_sum = True
    weakness = None

    while all_have_sum:
        n = numbers[i]

        n_has_sum = any(numbers[j] + numbers[k] == n
                        for j in range(i - 25, i)
                        for k in range(j, i))

        if not n_has_sum:
            weakness = numbers[i]

        all_have_sum = n_has_sum
        i += 1

    return weakness


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        numbers = [int(line.strip("\n")) for line in f]
        print(find_weakness(numbers))
