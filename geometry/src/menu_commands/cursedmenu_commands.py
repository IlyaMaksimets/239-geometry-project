from tkinter import *
from typing import Any
from ..other import canvas_clean
from ..other.decorators import points_deletion
from ..other import get_local_storage_path

# ----------------------------Неэкспортированные методы----------------------------


def points_move(x: float, y: float, move_x: Label, move_y: Label, move_x_entry: Entry, move_y_entry: Entry,
                points_move_button: Button) -> None:
    """
    Двигает точки на заданные величины x и y.

    :param x: float
    :param y: float
    :param move_x: Label
    :param move_y: Label
    :param move_x_entry: Entry
    :param move_y_entry: Entry
    :param points_move_button: Button
    :return: None
    """
    txt_file = open(get_local_storage_path(), 'r')
    lines = txt_file.readlines()
    txt_file.close()
    txt_file = open(get_local_storage_path(), 'w')
    for line in lines:
        coords = line.split()
        new_x = float(coords[0]) + x
        new_y = float(coords[1]) + y
        txt_file.write(f"{'%.1f' % new_x} {'%.1f' % new_y}\n")

    move_x.destroy()
    move_y.destroy()
    move_x_entry.destroy()
    move_y_entry.destroy()
    points_move_button.destroy()


# ----------------------------Экспортированные методы----------------------------

@points_deletion
@canvas_clean
def move_edit(canvas: Any) -> None:
    """
    Считывает х и у, на которые надо сдвинуть все точки.

    :param canvas: Any
    :return: None
    """
    move_x = Label(text="X: ")
    move_x.place(x=20, y=20, width=120, height=20)
    move_x_entry = Entry()
    move_x_entry.focus()
    move_x_entry.place(x=20, y=50, width=120, height=20)
    move_y = Label(text="Y: ")
    move_y.place(x=20, y=70, width=120, height=20)
    move_y_entry = Entry()
    move_y_entry.focus()
    move_y_entry.place(x=20, y=100, width=120, height=20)
    points_move_button = Button(text="Ввод",
                                command=lambda: points_move(float(move_x_entry.get()), float(move_y_entry.get()),
                                                            move_x,
                                                            move_y, move_x_entry, move_y_entry,
                                                            points_move_button))
    points_move_button.place(x=20, y=150, width=50, height=20)


@points_deletion
@canvas_clean
def mirror_edit(canvas: Any) -> None:
    """
    Отражает все точки относительно осей координат.

    :param canvas: Any
    :return: None
    """
    txt_file = open(get_local_storage_path(), 'r')
    lines = txt_file.readlines()
    txt_file.close()
    txt_file = open(get_local_storage_path(), 'w')
    for line in lines:
        coords = line.split()
        if (float(coords[0]) > 0 and float(coords[1])) > 0 or (float(coords[0]) < 0 and float(coords[1]) < 0):
            txt_file.write(f'{-float(coords[0])} {float(coords[1])}\n')
        if (float(coords[0]) > 0 and float(coords[1])) < 0 or (float(coords[0]) < 0 and float(coords[1]) > 0):
            txt_file.write(f'{float(coords[0])} {-float(coords[1])}\n')


@points_deletion
@canvas_clean
def rotate180_edit(canvas: Any):
    """
    Поворачивает картинку на 180 градусов.

    :param canvas: Any
    :return: None
    """
    txt_file = open(get_local_storage_path(), 'r')
    lines = txt_file.readlines()
    txt_file.close()
    txt_file = open(get_local_storage_path(), 'w')
    for line in lines:
        coords = line.split()
        txt_file.write(f'{-float(coords[0])} {-float(coords[1])}\n')
