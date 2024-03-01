from tkinter import *


class ModifiedCanvas(Canvas):
    """
    Класс, наследованный от класса Canvas из библиотки Tkinter. Включает в себя подготовку координатной плоскости и
    метод для ее повторной отрисовки.
    """

    def __init__(self, root: Tk) -> None:
        """
        Конструктор класса.

        :param root: Tk
        """
        super().__init__(root, width=1300, height=600, bg='white')
        super().pack()
        self.zoom = 1.0
        self.recreate_project_layout()

    def recreate_project_layout(self) -> None:
        """
        Метод для повторной отрисовки координатной плоскости.

        :return: None
        """
        super().create_rectangle(300, 0, 1300, 600, fill='white', outline="")
        super().create_line(301, 300, 1300, 300, arrow=LAST, width=2)
        super().create_line(800, 1, 800, 600, arrow=FIRST, width=2)
        super().create_text(1290, 285, text="Х", font='Calibri 20')
        super().create_text(790, 15, text="Y", font='Calibri 20')

        for i in range(0, 1000, 50):
            super().create_line(i + 300, 0, i + 300, 600)
            super().create_line(i + 300, 305, i + 300, 295)

            if i < 500:
                super().create_text(795 - i, 320, text='%.2f' % (int(i / 50 * (-1)) * self.zoom), font='Calibri 12')
            else:
                super().create_text(i + 295, 320, text='%.2f' % (int((i - 500) / 50) * self.zoom), font='Calibri 12')

        for i in range(0, 600, 50):
            super().create_line(805, i, 795, i)
            super().create_line(300, i, 1300, i)

            if i < 300:
                if i / 50 != 0:
                    super().create_text(790, 295 - i, text='%.2f' % (int(i / 50) * self.zoom), font='Calibri 12')
            else:
                if i - 345 > 0:
                    super().create_text(790, i - 5, text='%.2f' % (int((i - 345) / 50 * (-1) - 1) * self.zoom),
                                        font='Calibri 12')

    def set_zoom(self, value: int) -> None:
        """
        Устанавливает значение зума и перерисовывает координатную плоскость.

        :param value: int
        :return: None
        """
        self.zoom = value
        self.recreate_project_layout()
