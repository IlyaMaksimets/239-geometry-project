def get_x_cross(x1, y1, x2, y2, x3, y3, x4, y4) -> None:
    if x1 == x3 or x2 == x4:
        return None
    part1 = y4 - y1 + (x1 * (y3 - y1)) / (x3 - x1) - (x3 * (y4 - y2)) / (x3 - x1)
    part2 = (y3 - y1) / (x3 - x1) - (y4 - y2) / (x4 - x2)
    return part1 / part2


def count_ans() -> None:
    pass
