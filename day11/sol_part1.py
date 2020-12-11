#!/bin/python3

from copy import deepcopy


ADJACENT_DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


def count_adjacent(row_num, col_num, layout):
    n_rows = len(layout)
    n_cols = len(layout[0])
    adj_count = 0
    for dy, dx in ADJACENT_DIRS:
        if 0 <= row_num + dy < n_rows and 0 <= col_num + dx < n_cols:
            other_seat = layout[row_num + dy][col_num + dx]
            if other_seat == '#':
                adj_count += 1
    return adj_count


def do_layout_round(layout, occ_max, count_adjacent_fn):
    change_amount = 0
    next_layout = deepcopy(layout)
    for row_num, row in enumerate(layout):
        for col_num, seat in enumerate(row):
            if seat == 'L' or seat == '#':
                adj_count = count_adjacent_fn(row_num, col_num, layout)
                if seat == 'L' and adj_count == 0:
                    next_layout[row_num][col_num] = '#'
                    change_amount += 1
                elif seat == '#' and adj_count >= occ_max:
                    next_layout[row_num][col_num] = 'L'
                    change_amount += 1

    return next_layout, change_amount == 0


def count_occupied(layout):
    occ_count = 0
    for row in layout:
        for seat in row:
            if seat == '#':
                occ_count += 1
    return occ_count


def find_sol(layout):
    stable = False
    while not stable:
        layout, stable = do_layout_round(layout, 4, count_adjacent)
    return count_occupied(layout)

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        layout = [[ch for ch in line.strip("\n")] for line in f]
        print(find_sol(layout))
