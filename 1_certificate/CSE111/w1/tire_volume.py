"""
Author: Moroni Aguilera

This program calculates the volume of a tire based on user input for width, aspect ratio, and diameter. The formula used is:
Volume = (π * width^2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10^10

Changes:
- 050326: The program prompts the user to enter the width of the tire in millimeters, the aspect ratio, and the diameter of the wheel. It then calculates and displays the approximate volume of the tire.
- 070326: The program now also logs the input values and the calculated volume to a file named "volumes.txt" along with the current date, allowing for a record of all calculations made. Additionally, the user can choose to calculate the total volume for 2 or 4 tires, and this information is also logged.
"""
from datetime import datetime   

print("|------------------------------|\n|   Tire Volume Calculator     |\n|------------------------------|")

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volumen = (3.14159 * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000


print(f"The approximate volume of the tire is {volumen:.2f} liters.")

num_tires = input("Do you want to calculate the volume for 2 or 4 tires? (Enter 2, 4 or press Enter for just 1): ").strip()
if num_tires == "2":
    total_vol = volumen * 2
    print(f"The total volume for 2 tires is {total_vol:.2f} liters.")
elif num_tires == "4":
    total_vol = volumen * 4
    print(f"The total volume for 4 tires is {total_vol:.2f} liters.")
else:
    num_tires = "1"
    total_vol = volumen
    print(f"The total volume for 1 tire is {volumen:.2f} liters.")

current_date = datetime.now().date()

with open("volumes.txt", "a") as log_file:
   
    log_file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volumen:.2f}, {num_tires}, {total_vol:.2f}\n")
    