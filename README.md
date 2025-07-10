<!-- Banner -->
<h1 align="center">🕹️ Hangman Game - Python GUI Edition</h1>
<p align="center">
  A modern GUI-based Hangman game built using <b>Python</b> and <b>CustomTkinter</b>.<br/>
  Features ASCII Art, Score Tracking, External Word Support, and Multi-Round Gameplay!
</p>

---

## 📌 Overview

This project is a complete desktop version of the classic **Hangman Game**, developed with **Python** and a modern GUI powered by **CustomTkinter**.  
It includes a sleek user interface, support for external word files, visual hangman drawing with ASCII art, and a built-in scoring system over multiple rounds.

This project serves as both a **fun game** and a **strong portfolio project** to demonstrate your skills in GUI development, file handling, and game logic using Python.

---

## 🎮 Gameplay Instructions

- At launch, enter the number of rounds you want to play.
- You’ll be shown blank spaces for a randomly chosen word from `words.txt`.
- Guess one letter at a time using the input box.
- You have **6 chances** to guess the word correctly before the hangman is complete.
- Each correct guess fills in a letter.
- Incorrect guesses will build the ASCII hangman figure.
- After all rounds, your final **score** is displayed.

---

## 🛠️ Tech Stack Used

| Feature         | Technology          |
|----------------|---------------------|
| Language        | Python              |
| GUI Framework   | CustomTkinter       |
| HTTP/Word Fetch | requests (optional) |
| Packaging       | PyInstaller         |

---

## 🚀 Features

- ✅ **Modern GUI** using `customtkinter` (dark mode)
- ✅ **ASCII Art Hangman Drawing**
- ✅ **Multi-Round Mode** with scoring system
- ✅ **External Word File Support** (`words.txt`)
- ✅ **Input Validation** and error handling
- ✅ **Executable Packaging** with `.exe` support

---

## 🛠️ Installation Guide

Follow the steps below to set up the game on your computer:

---

### 1. 📂 Clone the Repository

```bash
git clone https://github.com/Bikash07-git/hangman-game-python.git
cd hangman-game-python

2. 📂 Install Dependencies
Install all required Python libraries from the requirements.txt file:
```bash
Copy code
pip install -r requirements.txt

pip install customtkinter requests

3. ▶️ Run the Game
python hangman_gui.py

