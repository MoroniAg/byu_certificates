"""
This program reads a list of products and their prices from a CSV file, then reads a customer's order from another CSV file. It calculates the subtotal, sales tax, and total for the order, and prints a receipt to the console. Additionally, it includes error handling for file-related issues and missing products in the catalog. An enhancement is included to print a coupon for one of the products ordered by the customer.

Author:Moroni Aguilera
Changes:
- 2026-04-03: Initial development and implementation of the receipt generation program.
- 2026-04-04: Added error handling for file-related issues and missing products in the catalog, Implemented the enhancement to print a coupon for one of the products ordered by the customer.


"""
import csv
from datetime import datetime

def read_dictionary(filename, key_column_index=None):
    dictionary = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if key_column_index is not None:
                dictionary[row[key_column_index]] = row
            else:
                dictionary[row[0]] = [ row[0], row[1], row[2]]
    
    return dictionary

def main():
    STORE_NAME = "Corner Market"
    TAX_RATE = 0.06

    try:
        products_dict = read_dictionary("products.csv", 0)

        subtotal = 0.0
        total_items = 0
        coupon_product = None
        print(STORE_NAME)
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print()
        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                prod_num = row[0]
                quantity = int(row[1])
                product = products_dict[prod_num]
                if len(product) == 2:
                    name = product[0]
                    price = float(product[1])
                else:
                    name = product[1]
                    price = float(product[2])

                line_total = quantity * price
                subtotal += line_total
                total_items += quantity
                coupon_product = (prod_num, name)
                print(f"{name}: {quantity} @ ${price:.2f} = ${line_total:.2f}")

        sales_tax = subtotal * TAX_RATE
        total = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print()
        print("Thank you for shopping at", STORE_NAME)
        if coupon_product is not None:
            cp_num, cp_name = coupon_product
            print()
            print("*** COUPON ***")
            print(f"Save 20% on your next purchase of: {cp_name} ({cp_num})")
            print("Present this coupon at checkout. Expires: 30 days from today.")
    except FileNotFoundError as e:
        print(f"Error: file not found - {e}")
    except PermissionError as e:
        print(f"Error: permission denied - {e}")
    except KeyError as e:
        print(f"Error: product not found in catalog - {e}")

if __name__ == "__main__":
  main()  