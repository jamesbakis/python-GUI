import tkinter as tk
from square import square
import enum

cells = []
pos = [3, 3]



def move_right(direction):    
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 6:
        pos[1] = 0
    else:
        pos[1] += 1
    cells[pos[0]][pos[1]].set_player()
    print("right")

def move_left(direction):   
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 0:
        pos[1] =6
    else:
        pos[1] -= 1
    cells[pos[0]][pos[1]].set_player()
    print("left")

def move_up(direction):   
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 0:
        pos[0] = 6
    else:
        pos[0] -= 1
    cells[pos[0]][pos[1]].set_player()
    print("up")

def move_down(direction):
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 6:
        pos[0] = 0
    else:
        pos[0] += 1
    cells[pos[0]][pos[1]].set_player()
    print("down")

def main():
    print("hello")
    root = tk.Tk()
    root.title("Collect Crystals")
    root.configure(background="red")
    root.geometry("700x700+300+0")
    # root.minsize(720, 480)
    # root.maxsize(720, 480)
    
    # label1 = tk.Label(root, text="Collect crystals!")
    # label2 = tk.Label(root, text="Avoid enemies!")
    
    # label1.pack()
    # label2.pack()
    

    for row in range(7):
        cells.append([])
        for col in range(7):
            cell = square(root, row, col)
            if row==col==3:
                 cell.set_player()
            else:
                cell.set_empty()
            cells[row].append(cell)
    root.bind("<Right>", move_right)
    root.bind("<Left>", move_left)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)

    root.mainloop()

if __name__ == "__main__":
    main()