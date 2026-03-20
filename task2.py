import random

# -------------------------------
# Hangman stages (visual)
# -------------------------------
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

# -------------------------------
# Words with categories
# -------------------------------
WORDS = {
    "python": "Programming Language",
    "guitar": "Musical Instrument",
    "football": "Sport",
    "computer": "Technology",
    "elephant": "Animal"
}

# -------------------------------
# Helper functions
# -------------------------------
def choose_word():
    word = random.choice(list(WORDS.keys()))
    return word, WORDS[word]

def display_word(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

def display_keyboard(guessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([c if c not in guessed else "_" for c in alphabet])

# -------------------------------
# Main game
# -------------------------------
def play_hangman():
    word, category = choose_word()
    guessed = set()
    wrong = 0
    hint_used = False
    score = 0

    print("\n🎮 WELCOME TO REAL HANGMAN 🎮")
    print("Category:", category)
    print("Type a letter | Type 'hint' to reveal one letter (once)")

    while wrong < 6:
        print(HANGMAN_PICS[wrong])
        print("\nWord :", display_word(word, guessed))
        print("Keys :", display_keyboard(guessed))
        print("Score:", score)

        guess = input("\nYour move: ").lower().strip()

        # Hint system (real-game style)
        if guess == "hint" and not hint_used:
            for c in word:
                if c not in guessed:
                    guessed.add(c)
                    print(f"💡 Hint revealed letter: {c}")
                    hint_used = True
                    wrong += 1
                    break
            continue

        if guess == "hint" and hint_used:
            print("⚠️ Hint already used!")
            continue

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter ONE valid letter.")
            continue

        if guess in guessed:
            print("⚠️ Already tried that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Correct!")
            score += 10
        else:
            print("❌ Wrong!")
            wrong += 1
            score -= 5

        # Win condition
        if all(c in guessed for c in word):
            print("\n🎉 YOU WIN!")
            print("Word:", word)
            print("Final Score:", score)
            return

    # Lose condition
    print(HANGMAN_PICS[6])
    print("\n💀 GAME OVER")
    print("The word was:", word)
    print("Final Score:", score)

# -------------------------------
# Replay loop
# -------------------------------
while True:
    play_hangman()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing!")
        break