🐍 SNAKE WATER GUN GAME:
A simple Python-based command-line interface (CLI) application that implements the classic "Snake, Water, Gun" game logic against an automated computer opponent.

📋 TABLE OF CONTENTS:
- [FEATURES](#-features)
- [GAME RULES](#-game-rules)
- [PREREQUISITES](#-prerequisites)
- [HOW TO RUN](#-how-to-run)
- [USAGE EXAMPLES](#-usage-examples)

✨ FEATURES:
- 🎯 **Dynamic rounds**: input your desired number of rounds at the start of each match session.
- 🤖 **AI opponent**: play against an automated computer choice powered by pseudorandom selection logic.
- 🎛️ **Session controls**: exit the game loop instantly at any point during active rounds by entering a termination code.
- 📊 **Score tracking**: real-time point distribution logs and absolute point counters for both the user and the computer.
- 🏆 **Result summary**: comprehensive post-match analysis dashboard detailing final scores and the ultimate match winner.

🎮 GAME RULES:
The core evaluation logic operates using standard hand-game triumph hierarchies:
- 🔫 **”Gun Beats Snake”** (Gun shoots snake)
- 🐍 **”Snake Beats Water”** (Snake drinks water)
- 💧 **”Water Beats Gun”** (Water rusts/drowns gun)
- Note: matches result in 1 point awarded for a win and 0 points awarded for draws or losses.

🚀 PREREQUISITES:
- Python 3.6 or higher

💻 HOW TO RUN:
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory:**
   ```bash
   cd snake-water-gun-game
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```

💡 USAGE EXAMPLES
1. Initiating the game loop

```text
WELCOME TO 'SNAKE WATER GUN'!

Number Of Rounds: 3
INSTRUCTIONS:
1. Gun Beats Snake.
2. Snake Beats Water.
3. Water Beats Gun.

1 Point For Win, 0 Point For Draw/Lose. READY?
```
2. Playing a round

```text
ROUND 1

Press 0-Stop
1-Snake
2-Water
3-Gun
Enter Number: 3
Computer Chose 1
Player Won
```
3. Match conclusion and summary

```text
GAME OVER!
YOU WON!
Your Score: 2
Computer's Score: 1
THANK YOU!
```

📄 LICENSE:
This project is open-source and free to modify for academic or personal projects.
