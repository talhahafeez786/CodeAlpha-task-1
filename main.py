import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        # Validate input: only single alphabetic characters are allowed
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
