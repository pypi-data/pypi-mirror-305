"""Menu class for Tkinter applications."""
import tkinter as tk
from tkinter import TclError


class Menu(tk.Menu):
    def __init__(self, root: tk.Tk, menu_items: list = []) -> None:
        super().__init__(root)
        self.menu_items = menu_items
        for menu_item in menu_items:
            self.add_command(label=menu_item.text, command=menu_item.command,
                             underline= menu_item.underline,)

    def enable(self, enable: bool) -> None:
        enable_menu_items(self, self.menu_items, enable)


class MenuItem():
    def __init__(
            self,
            text: str,
            command: object,
            dimmable: bool = False,
            **kwargs: dict,
            ) -> None:

        self.text: str = text
        self.command: object = command
        self.dimmable = dimmable
        self.underline = None

        if 'disabled' in kwargs:
            if kwargs['disabled']:
                self.disable()
        if 'underline' in kwargs:
            self.underline = kwargs['underline']

    def __repr__(self) -> str:
        return f'MenuItem: {self.text}'


def enable_menu_items(menu: Menu, menu_items: list, enable: bool) -> None:
    state = tk.NORMAL
    if not enable:
        state = tk.DISABLED
    for menu_item in menu_items:
        try:
            if menu_item.dimmable:
                menu.entryconfig(menu_item.text, state=state)
        except TclError:
            pass
