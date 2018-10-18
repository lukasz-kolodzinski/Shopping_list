"""
Project started: 18-10-2018
Developed by Lukasz Kolodzinski
"""

import tkinter as tk

class ShoppingList(tk.Tk):
    def __init__(self, products = None):
        super().__init__()

        if products is None:
            self.products = []
        else:
            self.products = products

shopping_list = ShoppingList()
shopping_list.mainloop()