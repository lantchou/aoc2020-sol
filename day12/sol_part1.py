ANGLE_TO_DIR = {
    0: "E",
    90: "N",
    180: "W",
    270: "S",
}

DIR_TO_ANGLE = {
    "E": 0,
    "N": 90,
    "W": 180,
    "S": 270,
}


with open("input.txt") as f:

    dir = "E"
    x, y = 0, 0
    for ins in f:
        ins_type = ins[0]
        ins_val = int(ins[1:])
        if ins_type in ("N", "S", "E", "W", "F"):
            # instruction is to move in a certain direction
            move_dir = dir if ins_type == "F" else ins_type
            if move_dir == "N" or move_dir == "S":
                dy = ins_val if move_dir == "N" else -ins_val
                y += dy
            else:
                dx = ins_val if move_dir == "E" else -ins_val
                x += dx
        else:
            # instruction is to rotate
            # we convert the direction the ship is currently facing into an angle on a unit circle
            angle = DIR_TO_ANGLE[dir]

            # rotate the angle by given value in given direction
            angle_diff = ins_val if ins_type == "L" else -ins_val
            new_angle = (angle + angle_diff) % 360

            # convert the new angle the ship is facing into a letter representing a direction again
            dir = ANGLE_TO_DIR[new_angle]

    print(abs(x) + abs(y))
