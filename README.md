# 🟩 Wordle Clone (Pygame Edition)

A classic Wordle-style word-guessing game built using **Python** and **Pygame**. The game randomly selects a five-letter word from a predefined list, and players have six attempts to guess it correctly.

---

## 🎮 How to Play

- Type your guess letter-by-letter.
- Press `SPACE` to submit your guess.
- Press `BACKSPACE` to delete a letter.
- The game ends when:
  - ✅ You guess the word correctly — **"You won!!"**
  - ❌ You use all six turns without success — **"You lost!"**

---

## 🧱 Game Features

- 🔤 Supports only 5-letter words.
- 🎨 Color feedback:
  - 🟩 **Green**: Correct letter in correct position
  - 🟨 **Yellow**: Correct letter in wrong position
  - ⚫ **Black/Uncolored**: Incorrect letter
- 🔁 Press `SPACE` after the game ends to start a new game.

---

## 📁 Project Structure

.
├── wordle_game.py       # Main game file (provided above)
├── words.py             # Contains list of 2316 five-letter words (e.g., [“apple”, “cabin”, …])

---

## 📦 Requirements

- Python 3.x
- Pygame

Install dependencies with:

```bash
pip install pygame



⸻

🚀 Run the Game

python wordle_game.py

Make sure words.py is in the same directory as the game file.

⸻

🧠 About words.py

The file words.py contains:

Words = ["apple", "brain", "cabin", ..., "zebra"]  # A list of 2316 5-letter words

This acts as the word bank from which the game randomly selects each round’s secret word.

⸻

🎨 Screenshots

Add screenshots here to showcase the game if desired.

⸻

🙌 Acknowledgments
	•	Pygame
	•	Inspired by the original Wordle game

---
