"""
Author: Moroni Aguilera

This program calculates the volume of a tire based on user input for width, aspect ratio, and diameter. The formula used is:
Volume = (π * width^2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10^10

Changes:
- 050326: The program prompts the user to enter the width of the tire in millimeters, the aspect ratio, and the diameter of the wheel. It then calculates and displays the approximate volume of the tire.

"""


width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volumen = (3.14159 * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume of the tire is {volumen:.2f} liters.")