def compute_receipt():
    total_price = 0

    while True:
        part_price = float(input("Enter the part price (enter 0 to finish): "))
        
        if part_price == 0:
            if total_price == 0:
                print("Invalid order!")
                return
            break

        if part_price < 0:
            print("Invalid price! Please enter a positive number.")
            continue

        # Calculate tax (20%)
        tax = part_price * 0.20

        # Calculate total price with tax
        total_price += (part_price + tax)

    customer_type = input("Enter customer type (special/regular): ").lower()

    if customer_type == "special":
        # Apply a 10% discount for special customers
        total_price *= 0.90

    print("\nReceipt:")
    print(f"Total price with tax: ${total_price:.2f}")

# Run the program
compute_receipt()