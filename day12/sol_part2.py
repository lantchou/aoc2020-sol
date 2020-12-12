from math import sin, cos, radians


def rotate_point(point, pivot_point, angle):
    """
    Rotate a point about a pivot point by a given angle.
    """
    x, y = point
    x_pivot, y_pivot = pivot_point

    angle = radians(angle)
    s = int(sin(angle))
    c = int(cos(angle))

    x -= x_pivot
    y -= y_pivot

    x_new = x * c - y * s + x_pivot
    y_new = x * s + y * c + y_pivot

    return x_new, y_new


with open("input.txt") as f:

    x_ship, y_ship = 0, 0
    x_wayp, y_wayp = 10, 1

    for ins in f:
        ins = ins.strip()
        ins_type = ins[0]
        ins_val = int(ins[1:])
        if ins_type in ("N", "S", "E", "W"):
            # instruction is to move waypoint in given direction
            if ins_type == "N" or ins_type == "S":
                dy = ins_val if ins_type == "N" else -ins_val
                y_wayp += dy
            else:
                dx = ins_val if ins_type == "E" else -ins_val
                x_wayp += dx
        elif ins_type in ("L", "R"):
            # instruction is to rotate waypoint about the ship by given angle
            angle = ins_val if ins_type == "L" else -ins_val
            x_wayp, y_wayp = rotate_point((x_wayp, y_wayp), (x_ship, y_ship), angle)
        else:
            # instruction is to move ship towards waypoint
            # first we move ship towards waypoint
            x_diff = x_wayp - x_ship
            y_diff = y_wayp - y_ship
            x_ship += x_diff * ins_val
            y_ship += y_diff * ins_val

            # then we also move waypoint so that its position relative to ship stays the same
            x_wayp = x_ship + x_diff
            y_wayp = y_ship + y_diff

    print(abs(x_ship) + abs(y_ship))
