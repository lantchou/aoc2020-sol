#!/bin/python3

from sol_part1 import count_occupied, do_layout_round, ADJACENT_DIRS


def count_adjacent(row_num, col_num, layout):
    n_rows = len(layout)
    n_cols = len(layout[0])
    adj_count = 0
    for dy, dx in ADJACENT_DIRS:
        y = row_num
        x = col_num
        stuck = False
        while 0 <= y + dy < n_rows and 0 <= x + dx < n_cols and not stuck:
            y += dy
            x += dx
            other_seat = layout[y][x]
            if other_seat == '#' or other_seat == 'L':
                if other_seat == '#':
                    adj_count += 1
                stuck = True

    return adj_count


def find_sol(layout):
    stable = False
    while not stable:
        layout, stable = do_layout_round(layout, 5, count_adjacent)
    return count_occupied(layout)


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        layout = [[ch for ch in line.strip("\n")] for line in f]
        print(find_sol(layout))

