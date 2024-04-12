from tkinter import *
from typing import Callable, Any


def canvas_clean(function: Callable[[Any], None]) -> Callable[[Any], None]:
    """
    Декоратор, очищающий поверхность слева от координатой плоскости.
    :param function: Callable[[Any], None]
    :return: Callable[[Any], None]
    """
    def inner(*args, **kwargs):
        Button(text="", bd=0, bg="white", state="disabled").place(x=0, y=0, width=300, height=600)
        return function(*args, **kwargs)

    return inner


def points_deletion(function: Callable[[Any], None]) -> Callable[[Any], None]:
    """
    Декоратор, очищающий координатную плоскость от точек.
    :param function: Callable[[Any], None]
    :return: Callable[[Any], None]
    """
    def inner(*args) -> None:
        args[0].recreate_project_layout()
        function(*args)

    return inner
