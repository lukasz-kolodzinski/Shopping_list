"""
Developed by Lukasz Kolodzinski
"""

import tkinter as tk
import tkinter.messagebox as msg

class TransferList(tk.Tk):
    def __init__(self, players = None):
        super().__init__()

        if players is None:
            self.players = []
        else:
            self.players = players

        self.app_canvas = tk.Canvas(self)
        self.names_bar_frame = tk.Frame(self.app_canvas)
        self.text_frame = tk.Frame(self)

        self.scrolling = tk.Scrollbar(self.app_canvas, orient="vertical", command=self.app_canvas.yview)
        self.app_canvas.configure(yscrollcommand=self.scrolling.set)

        self.title("Wish Transfer")
        self.geometry("500x700")

        self.create_wish = tk.Text(self.text_frame, height=2, bg = "white", fg="black")

        self.app_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrolling.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.app_canvas.create_window((0, 0), window=self.names_bar_frame, anchor="nw")
        self.create_wish.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_wish.focus_set()

        requested_player = tk.Label(self.names_bar_frame, text = "Add player's name here", bg = "lightgreen", fg = "black",
                                    pady=10, padx=190)
###        requested_player("<Button-1>", self.remove_task)
        self.players.append(requested_player)

        for player in self.players:
            player.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_player)
        self.color_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "lightblue", "fg": "black"}]

    def add_player(self, event=None):
        player_name = self.create_wish.get(1.0, tk.END).strip()

        if len(player_name) > 0:
            wished_player = tk.Label(self.names_bar_frame, text = player_name, pady=10)
            _, bar_style_choice = divmod(len(self.players), 2)
            color_scheme_choose = self.color_schemes[bar_style_choice]
            wished_player.configure(bg=color_scheme_choose["bg"])
            wished_player.configure(fg=color_scheme_choose["fg"])
            wished_player.pack(side=tk.TOP, fill=tk.X)
            self.players.append(wished_player)
        self.create_wish.delete(1.0, tk.END)

    def remove_player(self, event):
        player = event.widget
        if msg.askyesno("Confirm delte", "Do you want to delete {} ?".format(player.cget("text"))):
            self.players.remove(event.widget)
            event.widget.destroy()
            self.recolour_bars()

    

if __name__ == "__main__":
    transfer_list = TransferList()
    transfer_list.mainloop()