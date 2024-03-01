import sys
from tkinter import *
from typing import Any, Callable, List

from src.menu_commands import erase_edit, paste_edit, define_edit, delete_edit
from src.menu_commands import help_info, about_program_info
from src.menu_commands import keyboard_input, file_input, random_input
from src.menu_commands import move_edit, mirror_edit, rotate180_edit
from src.menu_commands import only_text_output, file_output, text_and_image_output
from src.menu_commands import write_point_pos


class MenuConfig:
    """
    Класс, описывающий все разделы и подрезделы меню, а также их функционал.

    Структура меню:

        - Ввод:

            - Клавиатура
            - Мышь
            - Файл
            - Random

        - Вывод:

            - Файл
            - Текст и изображение
            - Только текст

        - Редактирование:

            - Вставить
            - Заменить
            - Удалить
            - Очистить

        - Вычисление

        - Демонстрация

        - Справка:

            - Помощь
            - О программе

    """

    def __init__(self, mainmenu: Any, root: Tk, canvas: Any) -> None:
        """
        Конструктор класса.

        :param mainmenu: Any
        :param root: Tk
        :param canvas: Any
        :return: None
        """
        self.mainmenu = mainmenu
        self.root = root
        self.canvas = canvas
        self.inputmenu = Menu(mainmenu, tearoff=0)
        self.outputmenu = Menu(mainmenu, tearoff=0)
        self.editmenu = Menu(mainmenu, tearoff=0)
        self.cursedmenu = Menu(mainmenu, tearoff=0)
        self.infomenu = Menu(mainmenu, tearoff=0)
        self.mouse_input_allowed = False
        self.zoom = 1
        self.root.bind('<Button-1>', self.get_write_pos_function())

    def initialize_menu(self) -> None:
        """
        Инициализация меню программы.

        :return: None
        """
        self.inputmenu.add_command(label='Клавиатура',
                                   command=lambda: keyboard_input())
        self.inputmenu.add_command(label='Мышь',
                                   command=self.change_mouse_input_condition)
        self.inputmenu.add_command(label='Файл', command=lambda: file_input())
        self.inputmenu.add_command(label='Random',
                                   command=lambda: random_input(self.root))
        self.outputmenu.add_command(label='Файл', command=lambda: file_output())
        self.outputmenu.add_command(label='Текст и изображение',
                                    command=lambda: text_and_image_output(self.canvas, self.zoom))
        self.outputmenu.add_command(label='Только текст',
                                    command=lambda: only_text_output())

        self.editmenu.add_command(label='Вставить', command=lambda: paste_edit())
        self.editmenu.add_command(label='Заменить', command=lambda: define_edit())
        self.editmenu.add_command(label='Удалить',
                                  command=lambda: delete_edit())
        self.editmenu.add_command(label='Очистить',
                                  command=lambda: erase_edit(self.canvas))

        self.cursedmenu.add_command(label='Сдвиг',
                                    command=lambda: move_edit(self.canvas))
        self.cursedmenu.add_command(label='Отражение по четвертям',
                                    command=lambda: mirror_edit(self.canvas))
        self.cursedmenu.add_command(label='Поворот на 180 градусов',
                                    command=lambda: rotate180_edit(self.canvas))
        self.cursedmenu.add_command(label='Масштабирование',
                                    command=lambda: self.zoom_edit(self.canvas))

        self.infomenu.add_command(label='Помощь', command=lambda: help_info())
        self.infomenu.add_command(label='О программе',
                                  command=lambda: about_program_info())

        self.mainmenu.add_cascade(label='Ввод', menu=self.inputmenu)
        self.mainmenu.add_cascade(label='Вывод', menu=self.outputmenu)
        self.mainmenu.add_cascade(label='Редактирование', menu=self.editmenu)
        self.mainmenu.add_command(label='Вычисление', command={})
        self.mainmenu.add_cascade(label='Изменение', menu=self.cursedmenu)
        self.mainmenu.add_command(label='Демонстрация', command={})
        self.mainmenu.add_cascade(label='Справка', menu=self.infomenu)
        self.mainmenu.add_command(label='Выход', command=sys.exit)

    def change_mouse_input_condition(self) -> None:
        """
        Метод для изменения значения внутренней переменной, показывающей, разрешен ли в данный пользователю ввод
        точек при помощи нажатия на ЛКМ.

        :return: bool
        """
        Button(text="", bd=0, bg="white", state="disabled").place(x=0, y=0, width=250, height=600)
        self.mouse_input_allowed = not self.mouse_input_allowed
        self.root.unbind('<Button-1>')
        self.root.bind('<Button-1>', self.get_write_pos_function())

    def get_write_pos_function(self) -> [Callable[[Any], None], None]:
        """
        Предоставляет доступ к функции ввода мышью, если в меню была выбрана соответствующая опция.

        :return: [Callable[[Any], None], None]
        """
        if self.mouse_input_allowed:
            return write_point_pos

    def zoom_edit(self, canvas: Any) -> None:
        zoom_label = Label(text="Zoom: ")
        zoom_label.place(x=20, y=20, width=120, height=20)
        zooms = [0.01, 0.05, 0.1, 0.5, 0.75, 1, 2, 5]
        zoom_labels = []
        for i in range(8):
            zoom_labels.append(Label(text=f'{i + 1}) {zooms[i]}'))
            zoom_labels[i].place(x=20, y=40 + i * 20, width=120, height=20)
        zoom_entry = Entry()
        zoom_entry.focus()
        zoom_entry.place(x=20, y=200, width=120, height=20)
        set_zoom_button = Button(text="Ввод",
                                 command=lambda: self.set_zoom(int(zoom_entry.get()), zooms, zoom_labels, zoom_label,
                                                               zoom_entry,
                                                               set_zoom_button))
        set_zoom_button.place(x=20, y=220, width=50, height=20)

    def set_zoom(self, zoom: int, zooms: List, zoom_labels: List, zoom_label: Label, zoom_entry: Entry, set_zoom_button: Button) -> None:
        """
        Устанавливает значение зума, удаляет меню выбора масштаба и перерисовывает координатную плоскость.

        :param zoom: int
        :param zooms: List
        :param zoom_labels: List
        :param zoom_label: Label
        :param zoom_entry: Entry
        :param set_zoom_button: Button
        :return: None
        """
        self.zoom = float(zooms[zoom - 1])
        set_zoom_button.destroy()
        zoom_entry.destroy()
        zoom_label.destroy()
        for label in zoom_labels:
            label.destroy()
        self.canvas.set_zoom(self.zoom)
