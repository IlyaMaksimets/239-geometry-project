import tkinter.messagebox as mb
# ----------------------------Импортированные методы----------------------------


def help_info() -> None:
    """
    Всплывающее окно с информацией о меню программы.

    :return: None
    """
    info = open("src/menu_commands/info.txt", "r", encoding="utf-8").readlines()
    mb.showinfo("Помощь", "".join(info[:-1]))


def about_program_info() -> None:
    """
    Краткое описание программы.

    :return: None
    """
    info = open("src/menu_commands/info.txt", "r", encoding="utf-8").readlines()
    mb.showinfo("О программе", info[-1])