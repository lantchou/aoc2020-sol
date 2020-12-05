#!/usr/bin/python3


def get_seat_id(seat):
    row_l = 0
    row_r = 127
    for i in range(0, 7):
        mid = row_l + (row_r - row_l) // 2
        if seat[i] == "F":
            row_r = mid
        else:
            row_l = mid + 1

    col_l = 0
    col_r = 7
    for i in range(7, 10):
        mid = col_l + (col_r - col_l) // 2
        if seat[i] == "L":
            col_r = mid
        else:
            col_l = mid + 1

    return row_l * 8 + col_l


if __name__ == "__main__":
    with open("input.txt", "r") as f:

        max_seat_id = 0

        for seat in f:
            seat = seat.strip("\n")
            seat_id = get_seat_id(seat)
            if seat_id > max_seat_id:
                max_seat_id = seat_id

        print(max_seat_id)
