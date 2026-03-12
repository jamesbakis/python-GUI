import tkinter as tk
from square import square
import random, sys, os

cells = []
pos = [3, 3]
root = tk.Tk()
game_over = False
points = [0]
enemy_1 = [0, 0]
enemy_2 = [0, 6]
enemy_3 = [6, 3]
crystal = [0, 3]
enemy_all = (enemy_1, enemy_2, enemy_3)
units_all = (enemy_1, enemy_2, enemy_3, pos)

def enemy_collision():
    for enemy in enemy_all:
        if pos[0] == enemy[0] and pos[1] == enemy[1]:
            score.configure(text="Score: " + str(points[0]) + "\nGAME OVER \nPRESS \"R\" TO RESTART")
            score.pack_forget() 

            global game_over
            game_over = True

def crystal_collision(points):    
    for unit in units_all:
        if crystal[0] == unit[0] and crystal[1] == unit[1]:
            if unit[0] == pos[0] and unit[1] == pos[1]:
                points[0] += 1
                score.configure(text="Score: " + str(points[0]))
            x = random.randint(0, 6)
            y = random.randint(0, 6)
            while [x, y] in units_all:
                x = random.randint(0, 6)
                y = random.randint(0, 6)   
            cells[x][y].set_crystal()
            crystal[0] = x
            crystal[1] = y
            break


def move_right(direction): 
    global game_over
    if game_over:
        return 
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 6:
        pos[1] = 0
    else:
        pos[1] += 1
    cells[pos[0]][pos[1]].set_player()
    move_enemy(enemy_all)
    crystal_collision(points)
    enemy_collision()

def move_left(direction): 
    global game_over
    if game_over:
        return   
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 0:
        pos[1] =6
    else:
        pos[1] -= 1
    cells[pos[0]][pos[1]].set_player()
    move_enemy(enemy_all)
    crystal_collision(points)
    enemy_collision()

def move_up(direction): 
    global game_over
    if game_over:
        return    
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 0:
        pos[0] = 6
    else:
        pos[0] -= 1
    cells[pos[0]][pos[1]].set_player()
    move_enemy(enemy_all)
    crystal_collision(points)
    enemy_collision()

def move_down(direction): 
    global game_over
    if game_over:
        return 
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 6:
        pos[0] = 0
    else:
        pos[0] += 1
    cells[pos[0]][pos[1]].set_player()
    move_enemy(enemy_all)
    crystal_collision(points)
    enemy_collision()

def move_enemy(enemies):
    for enemy in enemies:
        if enemy[0] == pos[0] and enemy[1] == pos[1]:
            pass
        else:
            cells[enemy[0]][enemy[1]].set_empty()
        occupied = True
        while occupied:
            direction = random.randint(0, 3)
            if direction == 0: #left
                if enemy[1] == 0:
                    if [enemy[0], 6] not in enemies:
                        enemy[1] = 6
                        occupied = False
                else:
                    if [enemy[0], enemy[1] - 1] not in enemies:
                        enemy[1] -= 1
                        occupied = False
            elif direction == 1: #right
                if enemy[1] == 6:
                    if [enemy[0], 0] not in enemies:
                        enemy[1] = 0
                        occupied = False
                else:
                    if [enemy[0], enemy[1] + 1] not in enemies:
                        enemy[1] += 1
                        occupied = False
            elif direction == 2: #up
                if enemy[0] == 0:
                    if [6, enemy[1]] not in enemies:
                        enemy[0] = 6
                        occupied = False
                else:
                    if [enemy[0] - 1, enemy[1]] not in enemies:
                        enemy[0] -= 1
                        occupied = False
            elif direction == 3: #down
                if enemy[0] == 6:
                    if [0, enemy[1]] not in enemies:
                        enemy[0] = 0
                        occupied = False 
                else:
                    if [enemy[0] + 1, enemy[1]] not in enemies:
                        enemy[0] += 1
                        occupied = False  
        
        cells[enemy[0]][enemy[1]].set_enemy()

def reset_game(reset_button):
    global game_over, root, pos, enemy_1, enemy_2, enemy_3, crystal, enemy_all, units_all, points
    game_over = False
    points = [0]
    pos = [3, 3]
    enemy_1 = [0, 0]
    enemy_2 = [0, 6]
    enemy_3 = [6, 3]
    crystal = [0, 3]
    enemy_all = (enemy_1, enemy_2, enemy_3)
    units_all = (enemy_1, enemy_2, enemy_3, pos)
    score.configure(text="Score: " + str(points[0]))
    for row in range(7):
        for col in range(7):
            if row==col==3:
                 cells[row][col].set_player()
            elif (row == 0 and col == 0) or (row == 0 and col == 6) or (row == 6 and col == 3):
                cells[row][col].set_enemy()
            elif (row == 0 and col ==3):
                cells[row][col].set_crystal()
            else:
                cells[row][col].set_empty()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    print("hello")
    global root
    root.title("Collect Crystals")
    root.configure(background="red")
    root.geometry("700x700+300+0")
    game_square = resource_path("images/game_square.png")
    enemy_square = resource_path("images/enemy_square.png")
    crystal_square = resource_path("images/crystal_square.png")
    player_square = resource_path("images/player_square.png")
    
    for row in range(7):
        cells.append([])
        for col in range(7):
            cell = square(root, row, col, game_square, enemy_square, player_square, crystal_square, )
            if row==col==3:
                 cell.set_player()
            elif (row == 0 and col == 0) or (row == 0 and col == 6) or (row == 6 and col == 3):
                cell.set_enemy()
            elif (row == 0 and col ==3):
                cell.set_crystal()
            else:
                cell.set_empty()
            cells[row].append(cell)
    global score
    score = tk.Label(root, text="Score: " + str(points[0]))
    score.place(relx=0.5, rely=0.5, anchor='center')
    score.tkraise() 
    root.bind("<Right>", move_right)
    root.bind("<Left>", move_left)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)
    root.bind("<r>", reset_game)

    root.mainloop()

if __name__ == "__main__":
    main()