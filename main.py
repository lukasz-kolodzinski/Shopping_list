"""
Developed by Lukasz Kolodzinski
"""

import tkinter as tk

class TransferList(tk.Tk):
    def __init__(self, players = None):
        super().__init__()

        if players is None:
            self.players = []
        else:
            self.players = players

        self.title("Wish Transfer")
        self.geometry("500x700")

        requested_player = tk.Label(self, text = "Add player's name here", bg = "gray", fg = "blue")
        self.players.append(requested_player)

        for player in self.players:
            player.pack(side=tk.TOP, fill=tk.X)

        self.create_wish = tk.Text(self, height=2, bg = "white", fg="black")
        self.create_wish.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_wish.focus_set()
        self.bind("<Return>", self.add_player)

if __name__ == "__main__":
    transfer_list = TransferList()
    transfer_list.mainloop()