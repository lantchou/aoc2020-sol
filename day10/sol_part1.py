#!/usr/bin/python3


with open("input.txt", "r") as f:

    adapters = [int(adapter.strip("\n")) for adapter in f]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters = list(sorted(adapters))

    diffs_1 = 0
    diffs_3 = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff == 1:
            diffs_1 += 1
        elif diff == 3:
            diffs_3 += 1

    print(diffs_1 * diffs_3)
