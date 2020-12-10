#!/usr/bin/python3


def dfs(i, dp, adapters, ways) -> int:
    n_adapters = len(adapters)
    if dp[i] == True or i == len(adapters) - 1:
        ways[0] += 1
        return True
    elif dp[i] is None and i < len(adapters):
        if i + 1 < n_adapters and adapters[i + 1] - adapters[i] <= 3:
            if dfs(i + 1, dp, adapters, ways):
                dp[i] = True
        if i + 2 < n_adapters and adapters[i + 2] - adapters[i] <= 3:
            if dfs(i + 2, dp, adapters, ways):
                dp[i] = True
        if i + 3 < n_adapters and adapters[i + 3] - adapters[i] <= 3:
            if dfs(i + 3, dp, adapters, ways):
                dp[i] = True
    else:
        return False


with open("input.txt", "r") as f:

    adapters = [int(adapter.strip("\n")) for adapter in f]
    adapters.append(0)
    max_adapter = max(adapters)
    adapters.append(max_adapter + 3)
    adapters = list(sorted(adapters))
    print(adapters)

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

