from tkinter import *
from typing import List, Any

from ..other import get_local_storage_path, canvas_clean
from ..other.decorators import points_deletion


def get_x_cross(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> [None, List[
                    Any]]:
    if x1 == x3 or x2 == x4:
        return None
    part1 = (x1 * y2 - x2 * y1) * (x3 - x4) - (x1 - x2) * (x3 * y4 - x4 * y3)
    part2 = (x1 * y2 - x2 * y1) * (y3 - y4) - (y1 - y2) * (x3 * y4 - x4 * y3)
    part3 = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if part3 == 0:
        return None
    return [part1 / part3, part2 / part3]


def count_ans() -> List[float]:
    txt_file = open(get_local_storage_path(), 'r')
    lines = txt_file.readlines()
    txt_file.close()
    points = []
    ans_points = []
    for line in lines:
        point = line.split()
        points.append([float(point[0]), float(point[1])])
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                for m in range(len(lines)):
                    if i == j or i == k or i == m or j == k or j == m or k == m:
                        continue
                    ans = get_x_cross(*points[i], *points[j], *points[k], *points[m])
                    if ans is not None:
                        ans_points.append([*ans, *points[i], *points[j], *points[k],
                                           *points[m]])
    ans_point = ans_points[0]
    for i in range(1, len(ans_points)):
        if ans_points[i][0] ** 2 + ans_points[i][1] ** 2 < ans_point[0] ** 2 + ans_point[1] ** 2:
            ans_point = ans_points[i]
    x_y_label = Label(text=f"(X\', Y\'): {'%.2f' % ans_point[0]}, {'%.2f' % ans_point[1]}")
    x_y_label.place(x=20, y=20, width=120, height=20)
    x_y_1_label = Label(text=f"(X1, Y1): {ans_point[2]}, {ans_point[3]}")
    x_y_1_label.place(x=20, y=40, width=120, height=20)
    x_y_2_label = Label(text=f"(X2, Y2): {ans_point[4]}, {ans_point[5]}")
    x_y_2_label.place(x=20, y=60, width=120, height=20)
    x_y_3_label = Label(text=f"(X3, Y3): {ans_point[6]}, {ans_point[7]}")
    x_y_3_label.place(x=20, y=80, width=120, height=20)
    x_y_4_label = Label(text=f"(X4, Y4): {ans_point[8]}, {ans_point[9]}")
    x_y_4_label.place(x=20, y=100, width=120, height=20)
    return ans_point


@points_deletion
@canvas_clean
def demo_ans(canvas, zoom):
    ans_point = count_ans()
    canvas.create_line(800 + ans_point[2] * 50 / zoom, 300 + (-ans_point[3]) * 50 / zoom,
                       800 + ans_point[4] * 50 / zoom, 300 + (-ans_point[5]) * 50 / zoom)
    canvas.create_line(800 + ans_point[6] * 50 / zoom, 300 + (-ans_point[7]) * 50 / zoom,
                       800 + ans_point[8] * 50 / zoom, 300 + (-ans_point[9]) * 50 / zoom)
    canvas.create_oval(800 + ans_point[0] * 50 / zoom - 3, 300 + (-ans_point[1]) * 50 / zoom - 3,
                       800 + ans_point[0] * 50 / zoom + 3, 300 + (-ans_point[1]) * 50 / zoom + 3,
                       fill="black")
    canvas.create_oval(800 + ans_point[2] * 50 / zoom - 3, 300 + (-ans_point[3]) * 50 / zoom - 3,
                       800 + ans_point[2] * 50 / zoom + 3, 300 + (-ans_point[3]) * 50 / zoom + 3,
                       fill="black")
    canvas.create_oval(800 + ans_point[4] * 50 / zoom - 3, 300 + (-ans_point[5]) * 50 / zoom - 3,
                       800 + ans_point[4] * 50 / zoom + 3, 300 + (-ans_point[5]) * 50 / zoom + 3,
                       fill="black")
    canvas.create_oval(800 + ans_point[6] * 50 / zoom - 3, 300 + (-ans_point[7]) * 50 / zoom - 3,
                       800 + ans_point[6] * 50 / zoom + 3, 300 + (-ans_point[7]) * 50 / zoom + 3,
                       fill="black")
    canvas.create_oval(800 + ans_point[8] * 50 / zoom - 3, 300 + (-ans_point[9]) * 50 / zoom - 3,
                       800 + ans_point[8] * 50 / zoom + 3, 300 + (-ans_point[9]) * 50 / zoom + 3,
                       fill="black")
