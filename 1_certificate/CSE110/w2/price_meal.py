""" 
This program calculates the subtotal cost of a meal based on the number of children and adults, as well as their respective meal prices. It prompts the user for input and displays the subtotal.
Changes:
- 14-01-26: Add child and adult meal price inputs, calculate subtotal based on number of children and adults.
- 17-01-26: Add tax calculation and display total cost including tax, payment input, and change calculation, add validation for payment amount.
"""
import time

print("Meal Price Calculator for Jelys Restaurant \n")

child_meal_price = float(input("Insert the child's meal price: $"))
adult_meal_price = float(input("Insert the adult's meal price: $"))

num_children = int(input("Insert the number of children: "))
num_adults = int(input("Insert the number of adults: "))
tax_rate = float(input("Insert the tax rate (as a percentage, e.g., 7.5 for 7.5%): ")) / 100

print("-------------------------------------\nCalculating your total...\n")
time.sleep(1.5)
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"\nSubtotal: ${subtotal:.2f}")
sales_tax = subtotal * tax_rate
print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

payment_amount = float(input("\nInsert payment amount: $"))
if payment_amount < total:
    print("Insufficient payment amount. Please provide enough to cover the total.")
    exit()
change = payment_amount - total
print(f"Change: ${change:.2f}")

