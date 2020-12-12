from math import sin, cos, radians


def rotate_point(x, y, angle):
    """
    Rotate a point about the origin by a given angle.
    """

    angle = radians(angle)
    s = int(sin(angle))
    c = int(cos(angle))

    x_new = x * c - y * s
    y_new = x * s + y * c

    return x_new, y_new


with open("input.txt") as f:

    x_ship, y_ship = 0, 0
    x_wayp, y_wayp = 10, 1  # coordinates of waypoint relative to ship

    for ins in f:
        ins = ins.strip()
        ins_type = ins[0]
        ins_val = int(ins[1:])
        if ins_type in ("N", "S", "E", "W"):
            # Instruction is to move waypoint in given direction.
            if ins_type == "N" or ins_type == "S":
                dy = ins_val if ins_type == "N" else -ins_val
                y_wayp += dy
            else:
                dx = ins_val if ins_type == "E" else -ins_val
                x_wayp += dx
        elif ins_type in ("L", "R"):
            # Instruction is to rotate waypoint about the ship by given angle.
            # Because we keep the coordinates of the waypoint relative to the ship, we
            # pretend we are rotating the waypoint about the origin (0, 0).
            angle = ins_val if ins_type == "L" else -ins_val
            x_wayp, y_wayp = rotate_point(x_wayp, y_wayp, angle)
        else:
            # Instruction is to move ship towards waypoint.
            x_ship += x_wayp * ins_val
            y_ship += y_wayp * ins_val

    print(abs(x_ship) + abs(y_ship))
