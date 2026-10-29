def calculate_total():
    print("----------------------------------------")
    print("          TICKET BOOKING SYSTEM         ")
    print("----------------------------------------")
    print("1. General Admission ($25.00)")
    print("2. VIP Balcony ($60.00)")
    print("3. Student Pass ($12.00)")
    
    # Validate ticket selection
    while True:
        choice = input("\nSelect ticket category (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("Invalid input. Please enter 1, 2, or 3.")

    prices = {'1': 25.00, '2': 60.00, '3': 12.00}
    names = {'1': 'General Admission', '2': 'VIP Balcony', '3': 'Student Pass'}
    
    selected_price = prices[choice]
    selected_name = names[choice]

    # Validate ticket quantity
    while True:
        try:
            quantity = int(input(f"Enter quantity for {selected_name}: "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    # Optional snack package calculation
    snack_total = 0.0
    snack_input = input("Add snack vouchers at $8.00 each? (y/n): ").strip().lower()
    if snack_input == 'y':
        snack_total = 8.00 * quantity

    # Calculation logic
    subtotal = selected_price * quantity
    
    # 15% discount for 4 or more tickets
    discount = 0.0
    if quantity >= 4:
        discount = subtotal * 0.15

    total = (subtotal - discount) + snack_total

    # Summary output
    print("\n----------------------------------------")
    print("             ORDER SUMMARY              ")
    print("----------------------------------------")
    print(f"Ticket Type: {selected_name}")
    print(f"Quantity:    {quantity}")
    print(f"Subtotal:    ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount:   -${discount:.2f}")
    if snack_total > 0:
        print(f"Snacks:     +${snack_total:.2f}")
    print(f"Total Due:   ${total:.2f}")
    print("----------------------------------------")
    print("Transaction complete.")

if __name__ == "__main__":
    calculate_total()
