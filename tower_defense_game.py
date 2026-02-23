import tkinter as tk
import random

#project plan: tower defense (but like the only defense is the player)

#tower in center of window
    #sprite
    #hp bar

#player
    #sprite
    #movement 
    #attack - by running into enemies? 

#enemies
    #waves?
    #movement
    #attack
    #hp 
    #difficulty scaling
        #multiple types?
        #increase stats
            #dmg, hp, speed

# Constants
WIDTH = 800
HEIGHT = WIDTH*4//5

ENEMY_SIZE = 25 #they'll just be squares

# Functions
def tower_sprite(): # 50x75 p0x
    pattern = []

def player_sprite(): # 25x25 p0x
    pattern = []

def move_right(event):
    canvas.move(player, p_spd, 0)

def move_left(event):
    canvas.move(player, -p_spd, 0)

def move_up(event):
    canvas.move(player, 0, -p_spd)

def move_down(event):
    canvas.move(player, 0, p_spd)

def add_enemy_wave(num):
    pass

def move_enemies():
    pass

def collision(obj_a, obj_b):
    ax1, ay1, ax2, ay2 = canvas.bbox(obj_a)
    bx1, by1, bx2, by2 = canvas.bbox(obj_b)

def start():
    pass

def gameloop():
    pass

# Other Code/ Initial values
tower_img = tower_sprite()
player_img = player_sprite()

enemies = []
p_spd = 5
p_dmg = 5
t_hp = 500
e_spd = 5
e_dmg = 5
e_hp = 5

root = tk.Tk()
root.title("Tower Defense Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0B5A00")
canvas.pack()

tower = canvas.create_image(WIDTH//2, HEIGHT//2, image=tower_img, anchor="center")
player = canvas.create_image(WIDTH//2, HEIGHT*3//5, image=player_img, anchor="center")

root.bind("w", move_up)
root.bind("a", move_left)
root.bind("s", move_down)
root.bind("d", move_right)

root.mainloop()