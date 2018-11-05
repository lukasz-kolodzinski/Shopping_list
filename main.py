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

        requested_player = tk.Label(self, text = "Add player's name here", bg = "lightgreen", fg = "black")
        self.players.append(requested_player)

        for player in self.players:
            player.pack(side=tk.TOP, fill=tk.X)

        self.create_wish = tk.Text(self, height=2, bg = "white", fg="black")
        self.create_wish.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_wish.focus_set()
        self.bind("<Return>", self.add_player)
        self.color_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "lightblue", "fg": "black"}]

    def add_player(self, event=None):
        player_name = self.create_wish.get(1.0, tk.END).strip()
        if len(player_name) > 0:
            wished_player = tk.Label(self, text = player_name, pady=10)
            _, bar_style_choice = divmod(len(self.players), 2)
            color_scheme_choose = self.color_schemes[bar_style_choice]
            wished_player.configure(bg=color_scheme_choose["bg"])
            wished_player.configure(fg=color_scheme_choose["fg"])
            wished_player.pack(side=tk.TOP, fill=tk.X)
            self.players.append(wished_player)
        self.create_wish.delete(1.0, tk.END)

if __name__ == "__main__":
    transfer_list = TransferList()
    transfer_list.mainloop()