"""
Generates a funny story using user provided words.
Added a name input, extra print statements for story continuity, and input control methods.
Changes:
- 06-01-2026: Added name input and print statements for better story flow.
- 09-02-2026: added controls to format inputs in story. Added delay time for story generation effect.
"""

import time

print("Please enter the following: ")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb2 = input("Another verb: ")
verb3 = input("One more verb: ")
name = input("A name: ")
print("Your story is being generated...")
time.sleep(1)
print("\nYour story is ready: \n")
time.sleep(0.5)
print(f"The other day, I was really in trouble. It all started when I ({name.title()}) saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. {exclamation.title()}! I yelled. But all I ({name.title()}) could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family. Suddenly, {name.title()} decided to {verb.lower()} again, just to be sure.")