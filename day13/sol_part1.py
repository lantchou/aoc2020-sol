with open("input.txt") as f:
    first_timestamp = int(f.readline())
    bus_ids = [int(id) for id in f.readline().split(",") if id != "x"]

    timestamp = first_timestamp
    earliest_bus: int
    found_bus = False
    while not found_bus:
        for bus in bus_ids:
            if timestamp % bus == 0:
                earliest_bus = bus
                found_bus = True
                break

        if not found_bus:
            timestamp += 1

    print(earliest_bus * (timestamp - first_timestamp))

