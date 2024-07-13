import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        # List of words for the game
        self.words = ['python', 'hangman', 'challenge', 'programming', 'openai']
        # Randomly choose a word from the list
        self.word = random.choice(self.words)
        self.guessed_letters = set()  # Set to track guessed letters
        self.incorrect_guesses = 0  # Counter for incorrect guesses
        self.max_incorrect_guesses = 6  # Maximum allowed incorrect guesses
        
        self.create_widgets()  # Create the GUI widgets
        self.update_display()  # Initial display update

    def create_widgets(self):
        """Create and layout the GUI widgets."""
        # Label to display the current state of the word
        self.word_label = tk.Label(self.master, font=('Helvetica', 20))
        self.word_label.pack(pady=20)
        
        # Entry field for the user to input their guess
        self.guess_entry = tk.Entry(self.master, font=('Helvetica', 18))
        self.guess_entry.pack(pady=20)
        
        # Button to submit the guess
        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=('Helvetica', 18))
        self.guess_button.pack(pady=20)

        # Label to display guessed letters
        self.guessed_label = tk.Label(self.master, font=('Helvetica', 14))
        self.guessed_label.pack(pady=10)

        # Label to display remaining incorrect guesses
        self.remaining_label = tk.Label(self.master, font=('Helvetica', 14))
        self.remaining_label.pack(pady=10)

        # Label for displaying game messages
        self.message_label = tk.Label(self.master, font=('Helvetica', 14))
        self.message_label.pack(pady=10)

    def update_display(self):
        """Update the displayed word and other game state information."""
        # Create a string representation of the word with guessed letters revealed
        display_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.word_label.config(text=display_word)  # Update the word label
        self.guessed_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")  # Update guessed letters
        self.remaining_label.config(text=f"Incorrect guesses remaining: {self.max_incorrect_guesses - self.incorrect_guesses}")  # Update remaining guesses

        # Check if the game is over (loss)
        if self.incorrect_guesses >= self.max_incorrect_guesses:
            self.message_label.config(text=f"Game over! The word was: {self.word}")
            self.guess_button.config(state='disabled')  # Disable the guess button

        # Check if the game is won
        elif all(letter in self.guessed_letters for letter in self.word):
            self.message_label.config(text=f"Congratulations! You've guessed the word: {self.word}")
            self.guess_button.config(state='disabled')  # Disable the guess button

    def make_guess(self):
        """Process the user's letter guess."""
        guess = self.guess_entry.get().lower()  # Get the guess and convert to lowercase
        self.guess_entry.delete(0, tk.END)  # Clear the entry field

        # Validate input: must be a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Invalid input. Please guess a single letter.")
            return

        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            self.message_label.config(text="You have already guessed that letter.")
            return

        self.guessed_letters.add(guess)  # Add the guess to the set of guessed letters

        # Check if the guessed letter is in the word
        if guess in self.word:
            self.message_label.config(text=f"Good guess! '{guess}' is in the word.")
        else:
            self.message_label.config(text=f"Sorry, '{guess}' is not in the word.")
            self.incorrect_guesses += 1  # Increment the count of incorrect guesses

        self.update_display()  # Update the display after the guess

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = HangmanGame(root)  # Initialize the Hangman game
    root.mainloop()  # Run the Tkinter event loop
