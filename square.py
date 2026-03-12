import tkinter as tk

class square:
    def __init__(self, root, row, col, empty, enemy, player, crystal):
        self.root = root
        self.row = row
        self.col = col
        self.empty = tk.PhotoImage(file=empty)
        self.enemy = tk.PhotoImage(file=enemy)
        self.player = tk.PhotoImage(file=player)
        self.crystal = tk.PhotoImage(file=crystal)
        self.label = tk.Label(root, image=self.empty, borderwidth=0)
        self.label.grid(row=self.row, column=self.col)
        
    
    def set_empty(self):
        self.label.config(image=self.empty)

    def set_enemy(self):
        self.label.config(image=self.enemy)

    def set_player(self):
        self.label.config(image=self.player)
    
    def set_crystal(self):
        print("set crystal")
        self.label.config(image=self.crystal)