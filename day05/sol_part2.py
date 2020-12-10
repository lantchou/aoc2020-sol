#!/usr/bin/python3

from sol_part1 import get_seat_id

with open("input.txt", "r") as f:

    yours = []
    not_yours = []

    for seat in f:
        seat = seat.strip("\n")

        seat_id = get_seat_id(seat)
        not_yours.append(seat_id)
        yours.append(seat_id - 1)
        yours.append(seat_id + 1)

    yours.remove(max(yours))
    yours.remove(min(yours))

    diff = set(yours) - set(not_yours)
    your_seat = list(diff)[0]
    print(your_seat)
