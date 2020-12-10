#!/usr/bin/python3

def count_trees(step_right: int, step_down: int) -> int:
    with open("input.txt") as f:
        forest = f.read().splitlines()
        n_rows = len(forest)
        n_cols = len(forest[0])
        
        reached_end = False
        tree_count = 0
        col = 0
        for row in range(0, n_rows, step_down):
            if forest[row][col % n_cols] == '#':
                tree_count += 1
            col += step_right

        return tree_count


if __name__ == '__main__':
    print(count_trees(3, 1))

