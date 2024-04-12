from tkinter import *

from ..other import canvas_clean, get_local_storage_path
from ..classes.modified_canvas import ModifiedCanvas


# ----------------------------Неэкспортированные методы----------------------------


def create_file(file_name_label: Label, filename: str, file_name_button: Button, file_name_entry: Entry) -> None:
    """
    Функция создания текстового файла и его заполнения.

    :param file_name_label: Label
    :param filename: str
    :param file_name_button: Button
    :param file_name_entry: Entry
    :return: None
    """
    local_storage = open(get_local_storage_path(), 'r')
    lines = local_storage.readlines()
    local_storage.close()
    outputfile = open(f"geometry/src/output_files/{filename}.txt", 'w')
    for line in lines:
        outputfile.write(line)
    outputfile.close()
    local_storage = open(get_local_storage_path(), 'w')
    local_storage.close()
    file_name_button.destroy()
    file_name_entry.destroy()


# ----------------------------Экспортированные методы----------------------------

@canvas_clean
def file_output() -> None:
    """
    Функция для экспорта списка координат в текстовый файл.

    :return: None
    """
    file_name_label = Label(text="File name:")
    file_name_label.place(x=20, y=40, width=120, height=20)
    file_name_entry = Entry()
    file_name_entry.focus()
    file_name_entry.place(x=20, y=70, width=120, height=20)
    file_name_button = Button(text="Ввод",
                              command=lambda: create_file(file_name_label, file_name_entry.get(), file_name_button,
                                                          file_name_entry))
    file_name_button.place(x=20, y=120, width=50, height=20)


@canvas_clean
def text_and_image_output(canvas: ModifiedCanvas, zoom: float) -> None:
    """
    Функция для вывода координат в виде списка на зкран и на координатную плоскость в виде точек.

    :param canvas: ModifiedCanvas
    :param zoom: int
    :return: None
    """
    local_storage = open(get_local_storage_path())
    points = []
    xy_labels = []
    x_y_label = Label(text="X Y")
    x_y_label.place(x=20, y=20, width=120, height=20)
    y_for_list = 45
    for line in local_storage.readlines():
        points.append([float(line.split()[0]), float(line.split()[1])])
        xy_labels.append(Label(text=line))
        xy_labels[-1].place(x=20, y=y_for_list, width=120, height=30)
        y_for_list += 20
    local_storage.close()
    for point in points:
        canvas.create_oval(800 + point[0] * 50 / zoom - 3, 300 + (-point[1]) * 50 / zoom - 3,
                           800 + point[0] * 50 / zoom + 3,
                           300 + (-point[1]) * 50 / zoom + 3, fill="black")


@canvas_clean
def only_text_output() -> None:
    """
    Функция для вывода координат в виде списка на зкран.

    :return: None
    """
    local_storage = open(get_local_storage_path())
    xy_labels = []
    x_y_label = Label(text="X Y")
    x_y_label.place(x=20, y=20, width=120, height=20)
    y_for_list = 45
    for line in local_storage.readlines():
        xy_labels.append(Label(text=line))
        xy_labels[-1].place(x=20, y=y_for_list, width=120, height=30)
        y_for_list += 20
    local_storage.close()
