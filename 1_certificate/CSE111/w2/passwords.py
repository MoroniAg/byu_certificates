"""
"""

import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive):
    
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
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
    for ch in word:
        if ch in character_list:
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

def password_strength(password, min_length, strong_length):
    # 1) Dictionary check (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("'Password is a dictionary word and is not secure.")
        return 0

    # 2) Top passwords check (case-sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3) Minimum length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4) Long password
    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5) Complexity-based strength: base 1 + complexity (1..4)
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password strength (1+complexity): {strength}")
    return strength

def main():
    min_length = 10
    strong_length = 15
    print("Password checker — choose an option:")
    while True:
        print("\n1) Input a password to check")
        print("2) Quit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            password = input("Enter your password: ")
            _ = password_strength(password, min_length, strong_length)
        elif choice == "2":
            print("Exiting password checker.")
            break
        else:
            print("Invalid choice — enter 1 or 2.")

if __name__ == "__main__":
    main()