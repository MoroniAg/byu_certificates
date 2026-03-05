"""
|==============================|
|      SHOPPING CART APP       |
|==============================|

Author: Moroni Aguilera

Welcome to your digital shopping assistant! This program lets you build, review, and analyze your shopping cart with ease—track totals, averages, and even find the priciest and cheapest items in a snap.

This program implements a simple shopping cart system where users can add items, view the cart contents, and perform various analyses.

Changes:
- 260205: Initial implementation of shopping cart functionality.
- 260207: Added input validation for price and item removal, and improved user prompts.
"""


items = []
prices = []


print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add a new item")
    print("2. Display the contents of the shopping cart")
    print("3. Remove an item")
    print("4. Compute total")
    print("5. Compute average price")
    print("6. Show most expensive item")
    print("7. Show least expensive item")
    print("8. Quit")
    
    choice = input("Please enter an action: ")
    
    if choice == "1":
        item_name = input("What item would you like to add? ")
        while True:
            price_input = input("What is the price of the item? $")
            try:
                item_price = float(price_input)
                if item_price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
        items.append(item_name)
        prices.append(item_price)
        print(f"'{item_name}' has been added to the cart at ${item_price:.2f}.")

    elif choice == "2":
        if len(items) == 0:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for idx, (item, price) in enumerate(zip(items, prices), start=1):
                print(f"{idx}. {item} - ${price:.2f}")

    elif choice == "3":
        if len(items) == 0:
            print("The shopping cart is empty. Nothing to remove.")
        else:
            print("The contents of the shopping cart are:")
            for idx, (item, price) in enumerate(zip(items, prices), start=1):
                print(f"{idx}. {item} - ${price:.2f}")
            remove_input = input("Which item would you like to remove? (Enter the number): ")
            try:
                remove_idx = int(remove_input) - 1
                if 0 <= remove_idx < len(items):
                    removed_item = items.pop(remove_idx)
                    removed_price = prices.pop(remove_idx)
                    print(f"'{removed_item}' at ${removed_price:.2f} has been removed from the cart.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif choice == "4":
        if len(prices) == 0:
            print("The shopping cart is empty. Total is $0.00.")
        else:
            total = sum(prices)
            print(f"The total price of the items in the shopping cart is: ${total:.2f}")

    elif choice == "5":
        if len(prices) == 0:
            print("The shopping cart is empty. Cannot compute average.")
        else:
            avg = sum(prices) / len(prices)
            print(f"The average price of the items in the shopping cart is: ${avg:.2f}")

    elif choice == "6":
        if len(prices) == 0:
            print("The shopping cart is empty. No maximum item.")
        else:
            max_idx = prices.index(max(prices))
            print(f"The most expensive item is '{items[max_idx]}' at ${prices[max_idx]:.2f}")

    elif choice == "7":
        if len(prices) == 0:
            print("The shopping cart is empty. No minimum item.")
        else:
            min_idx = prices.index(min(prices))
            print(f"The least expensive item is '{items[min_idx]}' at ${prices[min_idx]:.2f}")

    elif choice == "8":
        print("Thank you for using the shopping cart program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")