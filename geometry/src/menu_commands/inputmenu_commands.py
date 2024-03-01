from random import randint as rd
from tkinter import *
from typing import Any
from ..other import canvas_clean, get_local_storage_path


# ----------------------------Неимпортированные методы----------------------------
def fill_points_list(n: int, number_of_points_label: Label, number_of_points_entry: Entry,
                     number_of_points_button: Button) -> None:
    """
    Функция заполнения local_storage случайными координатами в заданном количестве.

    :param n: int
    :param number_of_points_label: Label
    :param number_of_points_entry: Entry
    :param number_of_points_button: Button
    :return: None
    """
    globalPointsList = [(rd(-99, 99) / 10.0, rd(-49, 49) / 10.0) for _ in range(n)]
    txt_file = open(get_local_storage_path(), 'w')
    txt_file.seek(0)
    for a, b in globalPointsList:
        txt_file.write(f'{a} {b}\n')
    txt_file.close()
    number_of_points_label.destroy()
    number_of_points_entry.destroy()
    number_of_points_button.destroy()


def read_from_file(filename: str, file_name_button: Button, file_name_entry: Entry) -> None:
    """
    Фукнция, дублируюдщая содержимое файла с заданным названием в local_storage.

    :param filename: str
    :param file_name_button: Button
    :param file_name_entry: Entry
    :return: None
    """
    outputfile = open(f"src/input_files/{filename}.txt", 'r')
    lines = outputfile.readlines()
    outputfile.close()
    local_storage = open(get_local_storage_path(), 'w')
    for line in lines:
        local_storage.write(line)
    local_storage.close()
    file_name_button.destroy()
    file_name_entry.destroy()


def add_point_to_list(x: int, y: int, point_x: Label, point_y: Label, point_x_entry: Entry, point_y_entry: Entry,
                      point_add_button: Button) -> None:
    """
    Описание появится позже.
    :param x: int
    :param y: int
    :param point_x: Label
    :param point_y: Label
    :param point_x_entry: Entry
    :param point_y_entry: Entry
    :param point_add_button: Button
    :return: None
    """
    txt_file = open(get_local_storage_path(), 'a')
    txt_file.write(f'{x} {y}\n')
    txt_file.close()
    point_x.destroy()
    point_y.destroy()
    point_x_entry.destroy()
    point_y_entry.destroy()
    point_add_button.destroy()


# ----------------------------Импортированные методы----------------------------


@canvas_clean
def write_point_pos(event: Any) -> None:
    """
    Функция добавления в local_storage координаты точки в случае, если она не расположена вне координатной плоскости.

    :param event: Any
    :return: None
    """
    txt_file = open(get_local_storage_path(), 'a')
    x = float('%.1f' % ((event.x - 300) / 50 - 10))
    y = float('%.1f' % (-((event.y - 50) / 50 - 5)))
    if -10.0 < x < 10.0 and -5.0 < y < 5.0:
        txt_file.write(f'{x} {y}\n')
        txt_file.close()


@canvas_clean
def keyboard_input() -> None:
    """
    Функция для ввода координат при помощи клавиатуры.

    :return: None
    """
    point_x = Label(text="X: ")
    point_x.place(x=20, y=20, width=120, height=20)
    point_x_entry = Entry()
    point_x_entry.focus()
    point_x_entry.place(x=20, y=50, width=120, height=20)
    point_y = Label(text="Y: ")
    point_y.place(x=20, y=70, width=120, height=20)
    point_y_entry = Entry()
    point_y_entry.focus()
    point_y_entry.place(x=20, y=100, width=120, height=20)
    point_add_button = Button(text="Ввод",
                              command=lambda: add_point_to_list(int(point_x_entry.get()), int(point_y_entry.get()),
                                                                point_x,
                                                                point_y, point_x_entry, point_y_entry,
                                                                point_add_button))
    point_add_button.place(x=20, y=150, width=50, height=20)


@canvas_clean
def file_input() -> None:
    """
    Функция для импорта координат из папки input_files по названию файла.

    :return: None
    """
    file_name_label = Label(text="File name:")
    file_name_label.place(x=20, y=40, width=120, height=20)
    file_name_entry = Entry()
    file_name_entry.focus()
    file_name_entry.place(x=20, y=70, width=120, height=20)
    file_name_button = Button(text="Ввод",
                              command=lambda: read_from_file(file_name_entry.get(), file_name_button, file_name_entry))
    file_name_button.place(x=20, y=120, width=50, height=20)


@canvas_clean
def random_input(root: Tk) -> None:
    """
    Функция для генерации заданного кол-ва рандомных координат.

    :param root: Tk
    :return: None
    """
    number_of_points_label = Label(text="Количество точек: ")
    number_of_points_label.place(x=20, y=20, width=120, height=20)
    number_of_points_entry = Entry()
    number_of_points_entry.focus()
    number_of_points_entry.place(x=20, y=70, width=120, height=20)
    number_of_points_button = Button(text="Ввод",
                                     command=lambda: fill_points_list(int(number_of_points_entry.get()),
                                                                      number_of_points_label,
                                                                      number_of_points_entry, number_of_points_button))
    number_of_points_button.place(x=20, y=120, width=50, height=20)
