from tkinter import *
from .classes import MenuConfig
from .classes.modified_canvas import ModifiedCanvas


def main():
    while True:
        root = Tk()
        canvas = ModifiedCanvas(root)

        pn_control = Frame(root, height=70)
        pn_control.pack(side='top', fill='x')

        mainmenu = Menu(root)
        root.config(menu=mainmenu)
        menu_config = MenuConfig(mainmenu, root, canvas)
        menu_config.initialize_menu()
        root.mainloop()


if __name__ == "__main__":
    main()
