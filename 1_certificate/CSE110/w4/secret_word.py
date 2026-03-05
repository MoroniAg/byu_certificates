"""
This is a simple word guessing game where the player has to guess a predefined secret word.

Changes:
- 29-01-26: Initial version created with basic guessing functionality.
- 30-01-26: Added hints to indicate correct letters and their positions.
- 31-01-26: Improved user input handling and feedback messages, and added game type selection for different word lengths.
"""

print("Welcome to the world guessing game!")

secret_word = "python"
guess = ""
guess_count = 0

print(f"Select your game type: \n1. Easy (4-letter words)\n2. Medium (6-letter words)\n3. Hard (8-letter words)")

game_type = input("Enter the number corresponding to your choice: ")
if game_type == '1':
    secret_word = "code"
elif game_type == '2':
    secret_word = "python"
elif game_type == '3':
    secret_word = "computer"
else:
    print("Invalid choice. Defaulting to Medium (6-letter words).")

while guess != secret_word:
    guess = input("What is your guess? ")
    if len(guess) != len(secret_word):
        print(f"Your guess must be {len(secret_word)} letters long.")
        continue
    hints = ''
   
    for i in range(len(guess)):
        
        if secret_word[i].lower() == guess[i].lower():
            hints += guess[i].lower()+" "
        elif guess[i].lower() in secret_word.lower():
            hints += guess[i].upper()+" "
        else:
            hints += '_ '
                
    
    print("Hints: " + hints)
    guess_count += 1

print(f"Congratulations! You guessed the secret word '{secret_word}' in {guess_count} attempts.")