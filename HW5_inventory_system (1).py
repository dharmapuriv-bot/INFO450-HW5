# HW 5 - Python Supply Chain Buyer Order System
#
# This file contains the same Python program from my notebook.
# It uses a dictionary for the item catalog, a list for the purchase request,
# and functions to keep each part of the program organized.

# Step 1: Item catalog dictionary with exactly 7 items.
# The keys are item names and the values are unit prices.
catalog = {
    "printer paper": 6.50,
    "packing tape": 3.25,
    "shipping labels": 9.75,
    "nitrile gloves": 12.50,
    "box cutter": 4.95,
    "safety goggles": 8.25,
    "pallet wrap": 14.00
}

# Step 2: This function builds the purchase request list.
# The while loop keeps asking for items until the user types submit.
# Valid items are added to the request list, and invalid items are rejected.
def build_request(catalog):
    request = []

    while True:
        item = input("Enter an item to request (type 'submit' to finish): ").strip().lower()

        if item == "submit":
            break
        elif item in catalog:
            request.append(item)
            print(f"Added {item} to the purchase request.")
        else:
            print("Item not in catalog")

    return request

# Step 3: This function prints every requested item and calculates the subtotal.
def calculate_subtotal(request, catalog):
    subtotal = 0.0

    print("\nPurchase Request Summary:")
    for item in request:
        price = catalog[item]
        print(f"{item}: ${price:.2f}")
        subtotal += price

    print(f"\nSubtotal: ${subtotal:.2f}")
    return subtotal

# Step 4: This function adds the required shipping fee and 8% overhead.
def shipping_and_overhead(subtotal):
    shipping = 15.00
    overhead = 0.08 * subtotal
    final_total = subtotal + shipping + overhead

    print(f"Shipping: ${shipping:.2f}")
    print(f"Overhead (8%): ${overhead:.2f}")
    print(f"Final Total: ${final_total:.2f}")

    return final_total

# Step 5: Main function that runs the full workflow.
def main():
    request = build_request(catalog)
    subtotal = calculate_subtotal(request, catalog)
    final_total = shipping_and_overhead(subtotal)
    return final_total

# Test case used for the assignment:
# printer paper, packing tape, pallet wrap, submit
# Expected subtotal: $23.75
# Expected final total: $40.65

# Run the full interactive program when this file is executed.
if __name__ == "__main__":
    main()
