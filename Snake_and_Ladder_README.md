# 🐍🎲 Snake and Ladder Game (Tkinter + Pygame)

---

## 🧩 Overview
This is a **GUI-based Snake and Ladder game** built using **Python’s Tkinter**, **PIL (Pillow)**, and **Pygame** libraries.  
It allows **two players** to play alternately, roll dice, climb ladders, avoid snakes, and enjoy background music 🎶 — just like the classic board game!

---

## ⚙️ Features
✅ **Interactive GUI** using `Tkinter`  
✅ **Dynamic Dice Roll** with images for each number (1–6)  
✅ **Real-time Player Movement** on the board  
✅ **Snake 🐍 & Ladder 🪜 logic** implemented via dictionaries  
✅ **Background Music** using `pygame.mixer`  
✅ **Winner Announcement** with styled message  
✅ **Reset Button** to restart the game anytime  

---

## 🏗️ Project Structure
```
SnakeLadderGame/
│
├── snake_ladder.py          # Main Python file
├── assets/
│   ├── 1.png                # Dice image 1
│   ├── 2.png                # Dice image 2
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── board.png            # Game board image
│   ├── forest-ambience.mp3  # Background music
│   └── snake-hiss.mp3       # (Optional) Snake sound
└── README.md                # Documentation file
```

---

## 🧠 Game Logic
- The board coordinates are stored in a dictionary `Index` mapping numbers → `(x, y)` positions.  
- Players start at position `0`.  
- On each dice roll:
  - The player’s position is updated.
  - If they land on a **ladder**, they climb up 🪜.
  - If they land on a **snake**, they slide down 🐍.
  - A player must roll exactly enough to reach **100** to win 🏁.
- Turns alternate automatically unless the player rolls a **6**, which grants another turn.

---

## 🎵 Sound System
🎧 Background ambience plays continuously using:
```python
pygame.mixer.music.load("forest-ambience.mp3")
pygame.mixer.music.play(-1)
```

(Optional) You can also add effects like a **snake hiss sound**:
```python
snake_sound = pygame.mixer.Sound("snake-hiss.mp3")
snake_sound.play()
```

---

## 🎨 UI Design
| Element | Description |
|----------|--------------|
| 🎲 Dice | Changes image based on roll |
| 🔵 Player 1 Coin | Blue circular marker |
| 🔴 Player 2 Coin | Red circular marker |
| 🏁 Exit Button | Ends the game safely |
| 🎮 Player Buttons | Used to roll the dice alternately |

---

## 🧾 Code Highlights
```python
# Check for ladders
def check_Ladder(turn):
    if turn == 1 and pos1 in Ladder:
        pos1 = Ladder[pos1]

# Check for snakes
def check_Snake(turn):
    if turn == 1 and pos1 in Snake:
        pos1 = Snake[pos1]
```

```python
# Winner Declaration
def declare_winner(player):
    msg = f"Player {player} is the winner!"
    win_label = tk.Label(root, text=msg, bg='red', font=('Cursive', 30, 'bold'))
    win_label.place(x=300, y=300)
    reset_coins()
```

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pillow pygame
   ```
2. Update all file paths to match your local directories.
3. Run the script:
   ```bash
   python snake_ladder.py
   ```
4. Enjoy the game! 🎉

---

## 📸 Preview
> 🖼️ *(Add a screenshot or GIF of the game window here for your GitHub README.)*

---

## 💡 Future Improvements
- Add **AI opponent mode** 🤖  
- Add **sound effects for ladders/snakes** 🎵  
- Implement **score tracking and leaderboard** 🏆  
- Add **animations** for dice rolling and player movement 🎬  

---

## 👨‍💻 Author
**Developed by:** *Shobha Jangade*  
🎓 CSE (AI) Student, CSVTU  
💻 Languages: Python, C++, C  
