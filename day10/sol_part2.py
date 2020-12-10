#!/usr/bin/python3

with open("input.txt", "r") as f:

    adapters = [int(adapter.strip("\n")) for adapter in f]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters = list(sorted(adapters))

    ways = [0 for _ in range(len(adapters))]
    ways[0] = 1
    n_adapters = len(adapters)
    for i in range(1, len(adapters)):
        ways[i] += ways[i - 1]
        if i - 2 >= 0 and adapters[i] - adapters[i - 2] <= 3:
            ways[i] += ways[i - 2]
        if i - 3 >= 0 and adapters[i] - adapters[i - 3] <= 3:
            ways[i] += ways[i - 3]

    print(ways[len(adapters) - 1])

