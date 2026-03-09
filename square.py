import tkinter as tk
import random

class square:
    def __init__(self, root, row, col):
        self.root = root
        self.row = row
        self.col = col
        self.empty = tk.PhotoImage(file="game_square.png")
        # self.empty1 = tk.Label(root, image=self.empty, borderwidth=0)
        self.enemy = tk.PhotoImage(file="enemy_square.png")
        # self.enemy1 = tk.Label(root, image=self.enemy, borderwidth=0)
        self.player = tk.PhotoImage(file="player_square.png")
        # self.player1 = tk.Label(root, image=self.player, borderwidth=0)
        self.label = tk.Label(root, image=self.empty, borderwidth=0)
        self.label.grid(row=self.row, column=self.col)
        
    
    def set_empty(self):
        # self.empty1.grid(row=self.row, column=self.col)
        self.label.config(image=self.empty)

    def set_enemy(self):
        # self.enemy1.grid(row=self.row, column=self.col)
        self.label.config(image=self.enemy)

    def set_player(self):
        # self.player1.grid(row=self.row, column=self.col)
        self.label.config(image=self.player)