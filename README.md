# Rock Paper Scissors — Python Console Game

A fully-featured **console-based Rock Paper Scissors game** written in **Python 3.12**.  
This project demonstrates clean program structure, strong input validation, and professional coding practices.

---

## Features

- Best-of round system: **1, 3, or 5 rounds**
- Real-time scoreboard
- Tie tracking (ties do **not** count toward round wins)
- Full input validation (no crashes on bad input)
- Replay support
- Clean and well-documented source code

---

## Requirements

- **Python 3.12**

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/andriastheI/RockPaperScissors.git
```

2. **Navigate into the project**

```bash
cd RockPaperScissors
```

3. **Run the game**

```bash
python src/rock_paper_scissors.py
```

or

```bash
python3 src/rock_paper_scissors.py
```

---

## How to Play

1. Launch the game.
2. When prompted, choose whether to start the game.
3. Select how many rounds you want to play:
   - **a** → Best of 1  
   - **b** → Best of 3  
   - **c** → Best of 5  
4. Each round, enter:
   - **r** for Rock  
   - **p** for Paper  
   - **s** for Scissors  
5. The scoreboard updates after every round.
6. Ties are tracked but **do not count** toward winning the match.
7. After the match, choose whether you want to play again.

---

## Design Notes

- The program prevents invalid input from crashing the game.
- The match always ends with a winner.
- The code follows clean formatting and documentation standards.

---

## Project Structure

```text
RockPaperScissors/
│
├── src/
│   └── rock_paper_scissors.py
│
├── README.md
└── .gitignore
```

---

## Author

**Andrias Zelele**  
Computer Science Student  
Python 3.12

---

## Purpose

This project was created for educational purposes.

