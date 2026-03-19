"""
Password Strength Checker
This program checks the strength of a password based on several criteria:
1) It checks if the password is a dictionary word (case-insensitive).
2) It checks if the password is in a list of commonly used passwords (case-sensitive).
3) It checks if the password meets a minimum length requirement.
4) It checks if the password is long enough to be considered strong.
5) It evaluates the complexity of the password based on the presence of lowercase letters, uppercase letters, digits, and special characters, and assigns a strength score accordingly.

Author: Moroni Aguilera

Changes:
- 2026-03-12: Updated to include a menu for user interaction and improved error handling for file access. Added comments for clarity and maintainability.
- 2026-03-13: Refactored code to improve readability and modularity. Added more special characters to the list and enhanced the password strength evaluation logic. 
"""


LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                entry = line.rstrip("\n\r")
                if case_sensitive:
                    if word == entry:
                        return True
                else:
                    if word.lower() == entry.lower():
                        return True
    except FileNotFoundError:
        return False
    return False

def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False

def word_complexity(word):
    score = 0
    if word_has_character(word, LOWER):
        score += 1
    if word_has_character(word, UPPER):
        score += 1
    if word_has_character(word, DIGITS):
        score += 1
    if word_has_character(word, SPECIAL):
        score += 1
    return score

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("'Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password strength: {strength}")
    return strength

def save_password_check(password, strength, filename="passwords_checks.txt"):
    try:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a", encoding="utf-8") as fh:
            fh.write(f"{timestamp},{password},{strength}\n")
    except Exception as e:
        print(f"Error saving to {filename}: {e}")

def main():
    print("|--------------------------------------|\n|   Welcome to the Password Strength Checker!   |\n|--------------------------------------|")
    while True:
        print("\n1) Input a password to check")
        print("2) Quit")
        option = input("Enter option (1 or 2): ").strip()
        if option == "1":
            password = input("Enter your password: ")
            strength = password_strength(password)
            try:
                save_password_check(password, strength)
            except Exception:
                print("Could not save password check result.")
        elif option == "2":
            print("Exiting password checker.")
            break
        else:
            print("Invalid option — enter 1 or 2.")

if __name__ == "__main__":
    main()