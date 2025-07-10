import random
import customtkinter as ctk
from tkinter import messagebox

# Load words from external file
def load_words(filename='words.txt'):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file if line.strip()]

# ASCII stages
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.words = load_words()
        self.score = 0
        self.rounds = 0
        self.current_round = 0
        self.setup_ui()

    def setup_ui(self):
        self.master.title("Hangman Game")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title = ctk.CTkLabel(self.master, text="🎮 Hangman", font=("Arial", 32))
        self.title.pack(pady=10)

        self.round_label = ctk.CTkLabel(self.master, text="Enter number of rounds:")
        self.round_label.pack()

        self.round_entry = ctk.CTkEntry(self.master)
        self.round_entry.pack(pady=5)

        self.start_button = ctk.CTkButton(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=5)

        self.ascii_label = ctk.CTkLabel(self.master, text="", font=("Courier", 14), justify="left")
        self.ascii_label.pack()

        self.word_label = ctk.CTkLabel(self.master, text="", font=("Consolas", 24))
        self.word_label.pack(pady=5)

        self.guess_entry = ctk.CTkEntry(self.master)
        self.guess_entry.pack(pady=5)

        self.guess_button = ctk.CTkButton(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.score_label = ctk.CTkLabel(self.master, text="Score: 0")
        self.score_label.pack(pady=5)

        self.info_label = ctk.CTkLabel(self.master, text="")
        self.info_label.pack(pady=5)

        self.disable_gameplay()

    def start_game(self):
        try:
            self.rounds = int(self.round_entry.get())
            if self.rounds <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of rounds.")
            return

        self.current_round = 0
        self.score = 0
        self.next_round()

    def next_round(self):
        if self.current_round >= self.rounds:
            messagebox.showinfo("Game Over", f"🏁 Final Score: {self.score}/{self.rounds}")
            self.disable_gameplay()
            return

        self.word = random.choice(self.words)
        self.guessed = ['_'] * len(self.word)
        self.guessed_letters = set()
        self.attempts = 6
        self.current_round += 1

        self.update_display()
        self.enable_gameplay()

    def update_display(self):
        self.word_label.configure(text=" ".join(self.guessed))
        self.ascii_label.configure(text=HANGMAN_PICS[6 - self.attempts])
        self.score_label.configure(text=f"Round {self.current_round}/{self.rounds} | Score: {self.score}")
        self.info_label.configure(text="Guess a letter:")

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, 'end')

        if not guess.isalpha() or len(guess) != 1:
            self.info_label.configure(text="❌ Enter a single alphabet letter.")
            return

        if guess in self.guessed_letters:
            self.info_label.configure(text="🔁 Already guessed.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, char in enumerate(self.word):
                if char == guess:
                    self.guessed[i] = guess
            self.info_label.configure(text=f"✅ Good guess: {guess}")
        else:
            self.attempts -= 1
            self.info_label.configure(text=f"❌ Wrong guess: {guess}")

        self.update_display()

        if '_' not in self.guessed:
            self.score += 1
            messagebox.showinfo("Round Over", f"🎉 Correct! Word: {self.word}")
            self.next_round()
        elif self.attempts == 0:
            messagebox.showinfo("Round Over", f"💀 Out of tries! Word: {self.word}")
            self.next_round()

    def disable_gameplay(self):
        self.guess_entry.configure(state='disabled')
        self.guess_button.configure(state='disabled')

    def enable_gameplay(self):
        self.guess_entry.configure(state='normal')
        self.guess_button.configure(state='normal')

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("500x600")
    HangmanGame(app)
    app.mainloop()
