from tkinter import *
from ..other.decorators import points_deletion
from ..other import canvas_clean, get_local_storage_path
from ..classes.modified_canvas import ModifiedCanvas


# ----------------------------Неэкспортированные методы----------------------------


def define_point(point_x_label: Label, point_y_label: Label, point_x_define_label: Label, point_y_define_label: Label,
                 point_x: str, point_y: str, point_x_define: str, point_y_define: str, point_x_entry: Entry,
                 point_y_entry: Entry, point_x_define_entry: Entry,
                 point_y_define_entry: Entry, point_define_button: Button) -> None:
    """
    Заменяет координаты одной из точек из local_storage на введенные.

    :param point_x_label: Label
    :param point_y_label: Label
    :param point_x_define_label: Label
    :param point_y_define_label: Label
    :param point_x: str
    :param point_y: str
    :param point_x_define: str
    :param point_y_define: str
    :param point_x_entry: Entry
    :param point_y_entry: Entry
    :param point_x_define_entry: Entry
    :param point_y_define_entry: Entry
    :param point_define_button: Button
    :return: None
    """
    local_storage = open(get_local_storage_path(), 'r')
    lines = local_storage.readlines()
    local_storage.close()

    for i in range(len(lines)):
        coords = lines[i].split()
        if coords[0] == point_x and coords[1] == point_y:
            lines[i] = f"{point_x_define} {point_y_define}\n"
    local_storage = open(get_local_storage_path(), "w")
    for line in lines:
        local_storage.write(line)
    local_storage.close()
    point_x_entry.destroy()
    point_y_entry.destroy()
    point_x_define_entry.destroy()
    point_y_define_entry.destroy()
    point_define_button.destroy()
    point_x_label.destroy()
    point_y_label.destroy()
    point_x_define_label.destroy()
    point_y_define_label.destroy()


def add_point_to_list(x: float, y: float, point_x_label: Label, point_y_label: Label, point_x_entry: Entry,
                      point_y_entry: Entry,
                      point_add_button: Button) -> None:
    """
    Добавляет координаты точки в local_storage.

    :param x: float
    :param y: float
    :param point_x_label: Label
    :param point_y_label: Label
    :param point_x_entry: Entry
    :param point_y_entry: Entry
    :param point_add_button: Button
    :return: None
    """
    local_storage = open(get_local_storage_path(), 'a')
    local_storage.write(f'{x} {y}\n')
    local_storage.close()
    point_x_label.destroy()
    point_y_label.destroy()
    point_x_entry.destroy()
    point_y_entry.destroy()
    point_add_button.destroy()


def delete_point(x: float, y: float, point_x_label: Label, point_y_label: Label, point_x_entry: Entry,
                 point_y_entry: Entry,
                 point_add_button: Button) -> None:
    """
    Удаляет координаты точки из local_storage.

    :param x: int
    :param y: int
    :param point_x_label: Label
    :param point_y_label: Label
    :param point_x_entry: Entry
    :param point_y_entry: Entry
    :param point_add_button: Button
    :return: None
    """
    local_storage = open(get_local_storage_path(), 'r')
    lines = local_storage.readlines()
    local_storage.close()
    new_lines = []
    for line in lines:
        if line == f'{x} {y}\n':
            continue
        new_lines.append(line)
    local_storage = open(get_local_storage_path(), 'w')
    for line in new_lines:
        local_storage.write(line)
    point_x_label.destroy()
    point_y_label.destroy()
    point_x_entry.destroy()
    point_y_entry.destroy()
    point_add_button.destroy()


# ----------------------------Экспортированные методы----------------------------


@canvas_clean
def paste_edit() -> None:
    """
    Получает координаты точки, которую надо добавить в local_storage.

    :return: None
    """
    point_x_label = Label(text="X: ")
    point_x_label.place(x=20, y=20, width=120, height=20)
    point_x_entry = Entry()
    point_x_entry.focus()
    point_x_entry.place(x=20, y=50, width=120, height=20)
    point_y_label = Label(text="Y: ")
    point_y_label.place(x=20, y=70, width=120, height=20)
    point_y_entry = Entry()
    point_y_entry.focus()
    point_y_entry.place(x=20, y=100, width=120, height=20)
    point_add_button = Button(text="Ввод",
                              command=lambda: add_point_to_list(float(point_x_entry.get()), float(point_y_entry.get()),
                                                                point_x_label,
                                                                point_y_label, point_x_entry, point_y_entry,
                                                                point_add_button))
    point_add_button.place(x=20, y=150, width=50, height=20)


@canvas_clean
def define_edit() -> None:
    """
    Получает координаты точки, которую надо заменить в local_storage.

    :return: None
    """
    point_x_label = Label(text="X old: ")
    point_x_label.place(x=20, y=20, width=120, height=20)
    point_x_entry = Entry()
    point_x_entry.focus()
    point_x_entry.place(x=20, y=50, width=120, height=20)
    point_y_label = Label(text="Y old: ")
    point_y_label.place(x=20, y=80, width=120, height=20)
    point_y_entry = Entry()
    point_y_entry.focus()
    point_y_entry.place(x=20, y=110, width=120, height=20)
    point_x_define_label = Label(text="X new: ")
    point_x_define_label.place(x=20, y=140, width=120, height=20)
    point_x_define_entry = Entry()
    point_x_define_entry.focus()
    point_x_define_entry.place(x=20, y=170, width=120, height=20)
    point_y_define_label = Label(text="Y new: ")
    point_y_define_label.place(x=20, y=200, width=120, height=20)
    point_y_define_entry = Entry()
    point_y_define_entry.focus()
    point_y_define_entry.place(x=20, y=230, width=120, height=20)
    point_define_button = Button(text="Ввод",
                                 command=lambda: define_point(point_x_label, point_y_label, point_x_define_label,
                                                              point_y_define_label, point_x_entry.get(),
                                                              point_y_entry.get(),
                                                              point_x_define_entry.get(), point_y_define_entry.get(),
                                                              point_x_entry, point_y_entry, point_x_define_entry,
                                                              point_y_define_entry, point_define_button))
    point_define_button.place(x=20, y=270, width=50, height=20)


@canvas_clean
def delete_edit() -> None:
    """
    Получает координаты точки, которую надо удалить из local_storage.

    :return: None
    """
    point_x_label = Label(text="X: ")
    point_x_label.place(x=20, y=20, width=120, height=20)
    point_x_entry = Entry()
    point_x_entry.focus()
    point_x_entry.place(x=20, y=50, width=120, height=20)
    point_y_label = Label(text="Y: ")
    point_y_label.place(x=20, y=70, width=120, height=20)
    point_y_entry = Entry()
    point_y_entry.focus()
    point_y_entry.place(x=20, y=100, width=120, height=20)
    point_add_button = Button(text="Ввод",
                              command=lambda: delete_point(float(point_x_entry.get()), float(point_y_entry.get()),
                                                           point_x_label,
                                                           point_y_label, point_x_entry, point_y_entry,
                                                           point_add_button))
    point_add_button.place(x=20, y=150, width=50, height=20)


@canvas_clean
@points_deletion
def erase_edit(canvas: ModifiedCanvas) -> None:
    """
    Очищает плоскость от точек.

    :param canvas: ModifiedCanvas
    :return: None
    """
    pass
