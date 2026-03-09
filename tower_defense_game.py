import tkinter as tk
import random

# Constants
WIDTH = 800
HEIGHT = WIDTH*4//5
EDGES = ("N", "S", "E", "W")
UPGRADES = ("max hp up", "full heal", "speed up", "slow enemies", "weaken enemies")

# Functions
#sprites
def tower_sprite(): # 50x75 p0x
    pattern = [
        "01110000001110000001110000001110000001110000001110",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111000011111000011111000011111000011111000011111",
        "11111100111111100111111100111111100111111100111111",
        "11111111111111111111111111111111111111111111111111",
        "11111111111111111111111111111111111111111111111111",
        "01111111111111111111111111111111111111111111111110",
        "00111111111211111111211111111211111111211111111100",
        "00011111112121111112121111112121111112121111111000",
        "00001111121112111121112111121112111121112111110000",
        "00001111121112111121112111121112111121112111110000",
        "00000111211111211211111211211111211211111211100000",
        "00000111211111211211111211211111211211111211100000",
        "00000011111111111111111111111111111111111111000000",
        "00000011111111111111111111111111111111111111000000",
        "00000011111111111111111111111111111111111111000000",
        "00000011111111111111111111111111111111111111000000",
        "00000011111111111111111111111111111111111111000000",
        "00000111111111111111111111111111111111111111100000",
        "00000111111111111111111111111111111111111111100000",
        "00000111111111122222211111111222222111111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00000111111111222222221111112222222211111111100000",
        "00001111111111222222221111112222222211111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111111111111111111111111110000",
        "00001111111111111111111222211111111111111111110000",
        "00001111111111111111112222221111111111111111110000",
        "00001111111122211111112222221111111222111111110000",
        "00001111111222221111112222221111112222211111110000",
        "00011111111222221111112222221111112222211111111000",
        "00011111111222221111112222221111112222211111111000",
        "00011111111222221111112222221111112222211111111000",
        "00011111111222221111112222221111112222211111111000",
        "00011111111222221111111111111111112222211111111000",
        "00011111111111111111111111111111111111111111111000",
        "00011111111111111111111111111111111111111111111000",
        "00011111111111111111111111111111111111111111111000",
        "00011111111111111111111111111111111111111111111000",
        "00111111111111111111111111111111111111111111111100",
        "00111111111111111111111111111111111111111111111100",
        "00111122211111111111111111111111111111111222111100",
        "00111222221111111111112222221111111111112222211100",
        "00111222221111111111122222222111111111112222211100",
        "00111222221111111111222222222211111111112222211100",
        "00111222221111111111222222222211111111112222211100",
        "00111222221111111111222222222211111111112222211100",
        "01111222221111111111222222222211111111112222211110",
        "01111111111111111111222222222211111111111111111110",
        "01111111111111111111222222222211111111111111111110",
        "01111111111111111111222222222211111111111111111110",
        "01111111111111111111211222211211111111111111111110",
        "01111111111111111111222222222211111111111111111110",
        "11111111111111111111222222222211111111111111111111",
        "11111111111111111111222222222211111111111111111111",
        "11111111111111111111222222222211111111111111111111",
        "11111111111111111111222222222211111111111111111111",
    ]

    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#856337", (x,y))
            elif pattern[y][x] == "2":
                img.put("#D19754", (x,y))
    
    return img

def player_sprite(dir="right"): # 25x25 p0x
    if dir == "right":
        pattern = [
            "0000000000111110000000000",
            "0000000001111111000030000",
            "0000000011111111100333000",
            "0000000011121121103333300",
            "0000000011121121103333300",
            "0000000011111111103333300",
            "0000000011211121103333300",
            "0000330001122211003030300",
            "0333333330111110000030000",
            "0333333330001000000030000",
            "0333333330221220000030000",
            "0333333332112112200030000",
            "0333333331111111210030000",
            "0333333331111111211030000",
            "0333333331111111011222000",
            "0333333331111111001222000",
            "0033333301222221000222000",
            "0033333302111112000030000",
            "0003333001111111000030000",
            "0000330001110111000030000",
            "0000000001110111000030000",
            "0000000001110111000030000",
            "0000000222120212220030000",
            "0000002222220222222030000",
            "0000002222220222222000000",
        ]
    elif dir == "left":
        pattern = [
            "0000000000111110000000000",
            "0000300001111111000000000",
            "0003330011111111100000000",
            "0033333011211211100000000",
            "0033333011211211100000000",
            "0033333011111111100000000",
            "0033333011211121100000000",
            "0030303001122211000330000",
            "0000300000111110333333330",
            "0000300000001000333333330",
            "0000300000221220333333330",
            "0000300022112112333333330",
            "0000300121111111333333330",
            "0000301121111111333333330",
            "0002221101111111333333330",
            "0002221001111111333333330",
            "0002220001222221033333300",
            "0000300002111112033333300",
            "0000300001111111003333000",
            "0000300001110111000330000",
            "0000300001110111000000000",
            "0000300001110111000000000",
            "0000300222120212220000000",
            "0000302222220222222000000",
            "0000002222220222222000000",
        ]

    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#1E114E", (x,y))
            elif pattern[y][x] == "2":
                img.put("#1DE4D3", (x,y))
            elif pattern[y][x] == "3":
                img.put("#747474", (x,y))
    
    return img

def enemy_sprite(): # 25x25 p0x
    pattern = [
        "0000000000000000000000000",
        "0000000001111111000000000",
        "0000000011111111100000000",
        "0000000111111111110000000",
        "0000001111111111111000000",
        "0000001111111111111000000",
        "0000011111111111111100000",
        "0000011111111111111100000",
        "0000111111111111111110000",
        "0020111111111111111110200",
        "0222211111111111111122220",
        "2222222211111111122222222",
        "0022222222211122222222200",
        "0000122222222222222210000",
        "0000111122222222211110000",
        "0001011111122211111101000",
        "0001011111111111111101000",
        "0001001111122211111001000",
        "0001000111211121110001000",
        "0001000112111112110001000",
        "0001010111111111110101000",
        "0000110110111110110110000",
        "0000000110011100110000000",
        "0000000110000000110000000",
        "0000001110000000111000000",
    ]

    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#250303", (x,y))
            elif pattern[y][x] == "2":
                img.put("#D81212", (x,y))
    
    return img

#player movement
def move_right(event):
    global player, player_img
    canvas.move(player, p_spd, 0)
    player_img = player_sprite("right")
    x, y = canvas.coords(player)
    canvas.delete(player)
    player = canvas.create_image(x, y, image=player_img, anchor="center")

def move_left(event):
    global player_img, player
    canvas.move(player, -p_spd, 0)
    player_img = player_sprite("left")
    x, y = canvas.coords(player)
    canvas.delete(player)
    player = canvas.create_image(x, y, image=player_img, anchor="center")

def move_up(event):
    canvas.move(player, 0, -p_spd)

def move_down(event):
    canvas.move(player, 0, p_spd)

#enemy functions
def add_enemy_wave(num):
    for n in range(num):
        edge = random.choice(EDGES)
        if edge == "N":
            x = random.randint(0, WIDTH)
            y = 0
        elif edge == "S":
            x = random.randint(0, WIDTH)
            y = HEIGHT
        elif edge == "E":
            x = 0
            y = random.randint(0, HEIGHT)
        elif edge == "W":
            x = WIDTH
            y = random.randint(0, HEIGHT)
        e = canvas.create_image(x, y, image=enemy_img, anchor="center")
        enemies.append(e)

def move_enemies(e, dir="center"):
    x, y = canvas.coords(e)
    
    if x < WIDTH//2: #east
        if y < HEIGHT//2: #northeast
            dx = e_spd//2
            dy = e_spd//2
        elif y > HEIGHT//2: #southeast
            dx = e_spd//2
            dy = -e_spd//2
        else:
            dx = e_spd
            dy = 0
    elif x > WIDTH//2: #west
        if y < HEIGHT//2: #northwest
            dx = -e_spd//2
            dy = e_spd//2
        elif y > HEIGHT//2: #southwest
            dx = -e_spd//2
            dy = -e_spd//2
        else:
            dx = -e_spd
            dy = 0
    elif y < HEIGHT//2: #north
        dx = 0
        dy = e_spd
    elif y > HEIGHT//2: #south
        dx = 0
        dy = -e_spd
    else:
        return
    
    if dir == "center":
        canvas.move(e, dx, dy)
    elif dir == "reverse":
        canvas.move(e, -dx, -dy)

#generic collision check
def collision(obj_a, obj_b):
    ax1, ay1, ax2, ay2 = canvas.bbox(obj_a)
    bx1, by1, bx2, by2 = canvas.bbox(obj_b)

    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

#running the game
def start(event):
    # initial values
    global enemies, p_spd, p_dmg, t_hp_max, t_hp, e_spd, e_dmg, wave_size, wave_num, wave_countdown, wave_text_size, tower, player, t_hp_bar, t_max_bar
    if not alive:
        #reset everything
        canvas.delete("all")

        enemies = []
        p_spd = 15
        p_dmg = 5
        t_hp_max = 100
        t_hp = t_hp_max
        e_spd = 10
        e_dmg = 0
        wave_size = 3
        wave_num = 0
        wave_countdown = 10
        wave_text_size = 25

        tower = canvas.create_image(WIDTH//2, HEIGHT//2, image=tower_img, anchor="center")
        player = canvas.create_image(WIDTH//2, HEIGHT*3//5, image=player_img, anchor="center")
        t_max_bar = canvas.create_rectangle(WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2+t_hp_max//2, HEIGHT//2-45, fill="#494949")
        t_hp_bar = canvas.create_rectangle(WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2+t_hp_max//2, HEIGHT//2-45, fill="#A3345F")
        
        wave_start()

def game_loop():
    global t_hp, wave_num
    for e in enemies[:]:
        if collision(e, player):
            canvas.delete(e)
            enemies.remove(e)
        elif collision(e, tower):
            t_hp -= e_dmg
            canvas.coords(t_hp_bar, WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2-t_hp_max//2+t_hp, HEIGHT//2-45)
            #reverse movement of enemy out of tower (so they end up kinda bouncing at the edges of the tower)
            while collision(e, tower):
                move_enemies(e, "reverse") 
        else:
            move_enemies(e)
    
    if t_hp <= 0:
        game_over()
        return

    if len(enemies) == 0:
        power_up()
        wave_num += 1
        root.after(1000, wave_start)
    else:
        root.after(250, game_loop)

def wave_start():
    global wave_size, wave_countdown, wave_text_size, e_dmg, e_spd
    canvas.delete("countdown")
    canvas.create_text(WIDTH//2, HEIGHT//4, text=f"Wave {wave_num+1} starts in {wave_countdown}", fill="#FFFFFF", font=("Arial", wave_text_size), tags="countdown")
    if wave_countdown <= 0:
        canvas.delete("countdown")
        wave_size += 2
        wave_countdown = 10
        wave_text_size = 25
        if wave_num % 5 == 0:
            e_dmg += 1
            e_spd += 5

        add_enemy_wave(wave_size)
        game_loop()
    else:
        wave_countdown -= 1
        wave_text_size += 5
        root.after(1000, wave_start)

def power_up():
    global t_hp_max, t_hp, p_spd, e_spd, e_dmg
    power = random.choice(UPGRADES)
    canvas.create_text(WIDTH//2, HEIGHT*3//4, text=f"wave clear power up: {power}", fill="#3ACCF0", font=("Arial", 24), tags="countdown")
    if power == "full heal":
        t_hp = t_hp_max
        canvas.coords(t_hp_bar, WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2+t_hp_max//2, HEIGHT//2-45)
    elif power == "max hp up":
        t_hp_max += 20
        t_hp += 20
        canvas.coords(t_max_bar, WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2+t_hp_max//2, HEIGHT//2-45,)
        canvas.coords(t_hp_bar, WIDTH//2-t_hp_max//2, HEIGHT//2-50, WIDTH//2-t_hp_max//2+t_hp, HEIGHT//2-45,)
    elif power == "speed up":
        p_spd += 5
    elif power == "slow enemies":
        e_spd -= 5
        if e_spd < 5:
            e_spd = 5
    elif power == "weaken enemies":
        e_dmg -= 1
        if e_dmg < 1:
            e_dmg = 1
    else:
        return

def game_over():
    global alive
    canvas.delete("all")
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#000000")
    canvas.create_text(WIDTH//2, HEIGHT//3, text="Waves Cleared:" + str(wave_num), fill="#7F15A8", font=("Arial", 40))
    canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="#790000", font=("Arial", 50))
    canvas.create_text(WIDTH//2, HEIGHT*2//3, text="Press Space to Play Again", fill="#858585", font=("Arial", 35))
    alive = False

# Other Code

#window
root = tk.Tk()
root.title("Tower Wave Defense")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0B5A00")
canvas.pack()

tower_img = tower_sprite()
player_img = player_sprite()
enemy_img = enemy_sprite()

#keybinds
root.bind("w", move_up)
root.bind("a", move_left)
root.bind("s", move_down)
root.bind("d", move_right)
root.bind("<space>", start)

canvas.create_text(WIDTH//2, HEIGHT//3, text="Tower Wave Defense", fill="#6D1202", font=("Arial", 50))
canvas.create_text(WIDTH//2, HEIGHT//2, text="Press Space To Start", fill="#B6B6B6", font=("Arial", 60))
canvas.create_text(WIDTH//2, HEIGHT*2//3, text="W A S D for movement", fill= "#888787", font=("Arial", 30))
alive = False

root.mainloop()