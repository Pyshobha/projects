import tkinter as tk
from PIL import ImageTk, Image
import random
import pygame

def start_game():
    global im, b1, b2

    # Player buttons
    b1.place(x=1000, y=400)
    b2.place(x=1000, y=500)
    
    # Initialize Pygame
    pygame.mixer.init()

    # Load and play background music
    pygame.mixer.music.load(r"C:\Users\Owner\Downloads\forest-ambience-296528.mp3") 
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

   # global snake_sound
   # snake_sound = pygame.mixer.Sound(r"C:\Users\Owner\Downloads\snake-hiss-95241.mp3")  

   

    # Dice image to show
    im = Image.open(r"C:\Users\Owner\Pictures\Screenshots\images.png")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)

    b = tk.Button(root, image=im, height=80, width=80)
    b.place(x=1058, y=200)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", height=3, width=20, fg="red", bg="yellow", font=('Cursive', 14, 'bold'), activebackground='red', command=root.destroy)
    exit_button.place(x=1000, y=20)

def reset_coins():
    global pos1, pos2
    pos1 = 0
    pos2 = 0
    player_1.place(x=10, y=720)
    player_2.place(x=50, y=720)

def load_dice_images():
    global Dice
    Dice = []
    names = [r"C:\Users\Owner\Downloads\1.png", r"C:\Users\Owner\Downloads\2.png",
             r"C:\Users\Owner\Downloads\3.png", r"C:\Users\Owner\Downloads\4.png",
             r"C:\Users\Owner\Downloads\5.png", r"C:\Users\Owner\Downloads\6.png"]
    for name in names:
        im = Image.open(name)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)

def check_Ladder(turn):
    global pos1, pos2
    if turn == 1 and pos1 in Ladder:
        pos1 = Ladder[pos1]
    elif turn == 2 and pos2 in Ladder:
        pos2 = Ladder[pos2]

def check_Snake(turn):
    global pos1, pos2
    if turn == 1 and pos1 in Snake:
        pos1 = Snake[pos1]
    elif turn == 2 and pos2 in Snake:
        pos2 = Snake[pos2]

def roll_dice():
    global turn, pos1, pos2, b1, b2

    # Roll the dice and display result
    r = random.randint(1, 6)
    print(f"Turn: {turn}, Roll: {r}")
    dice_button = tk.Button(root, image=Dice[r - 1], height=80, width=80)
    dice_button.place(x=1058, y=200)

    # Move player based on turn
    if turn == 1:
        if pos1 + r <= 100:
            pos1 += r
            move_coin(turn, pos1)
            check_Ladder(turn)
            check_Snake(turn)
            move_coin(turn, pos1)  # Move again if affected by ladder/snake
            if pos1 == 100:
                declare_winner(1)
            elif r != 6:  # Change turn if not a 6
                turn = 2
                b1.configure(state='disabled')
                b2.configure(state='normal')
    else:
        if pos2 + r <= 100:
            pos2 += r
            move_coin(turn, pos2)
            check_Ladder(turn)
            check_Snake(turn)
            move_coin(turn, pos2)  # Move again if affected by ladder/snake
            if pos2 == 100:
                declare_winner(2)
            elif r != 6:  # Change turn if not a 6
                turn = 1
                b2.configure(state='disabled')
                b1.configure(state='normal')

def declare_winner(player):
    msg = f"Player {player} is the winner!"
    win_label = tk.Label(root, text=msg, height=2, width=20, bg='red', font=('Cursive', 30, 'bold'))
    win_label.place(x=300, y=300)
    reset_coins()

def move_coin(turn, pos):
    if turn == 1:
        player_1.place(x=Index[pos][0], y=Index[pos][1])
    else:
        player_2.place(x=Index[pos][0], y=Index[pos][1])

def get_Index():
    global Index
    Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    row = 75
    Index = {}
    i = 0
    for x in range(1, 11):
        col = 50
        for y in range(1, 11):
            Index[Num[i]] = (col, row)
            col += 70
            i += 1
        row += 67

# Game setup
root = tk.Tk()
root.geometry("1200x800")
root.title("Snake and Ladder Game")

# Board background
img_path = r"C:\Users\Owner\Downloads\Screenshot 2024-10-18 214305 (2).png"
img = Image.open(img_path)
photo = ImageTk.PhotoImage(img)
board_label = tk.Label(root, image=photo)
board_label.place(x=0, y=0)

# Player buttons and coins
b1 = tk.Button(root, text="Player 1", height=3, width=20, fg="red", bg="cyan", font=('Cursive', 14, 'bold'), activebackground='blue', command=roll_dice)
b2 = tk.Button(root, text="Player 2", height=3, width=20, fg="red", bg="orange", font=('Cursive', 14, 'bold'), activebackground='red', command=roll_dice)

player_1 = tk.Canvas(root, width=25, height=25)
player_1.create_oval(4, 4, 27, 27, fill='blue')
player_2 = tk.Canvas(root, width=25, height=25)
player_2.create_oval(4, 4, 27, 27, fill='red')

# Game variables
turn = 1
pos1 = pos2 = 0
Ladder = {4: 56, 12: 50, 14: 55, 22: 58, 41: 79, 54: 88}
Snake = {96: 42, 94: 71, 75: 32, 48: 16, 37: 3, 28: 10}

# Initialize game
reset_coins()
get_Index()
load_dice_images()
start_game()

root.mainloop()
