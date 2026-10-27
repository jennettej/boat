def main():
    """
    Main function for a boat ticket purchasing system
    Allows customers to select seats, add tickets to a cart, view ticket prices,
    and the running total, cancel purchases, and complete purchases.
    Also tracks the sold seats and total revenue.
    """

    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Stores the letters for all 26 rows of seats
    seats_per_row = 8 # Store the number of seats in each row
    total_seats = 26 * seats_per_row # Calculate total number of seats on the boat
    base_price = 10 # Store the base price for aisle seats
    sold_seats = [] # Store seats that have been sold
    total_revenue = 0 # Track the total revenue from completed purchases

    while True: # Continue allowing customers the purchase tickets
        # Create an empty cart for the customer
        cart = []
        cart_total = 0

        print("Welcome to the Boat Ticket Purchasing System!")
        print("Available seats: Rows A-Z, Seats 1-8")
        print("Window seats (1 and 8): $11")
        print("Middle seats (2, 3, 6, and 7): $9")
        print("Aisle seats (4 and 5): $10")

        # Allow the customer to select multiple seats
        while True:
            print(f"\nCurrent cart: {cart}")
            print(f"Current cart total: ${cart_total}")

            # Ask the customer what seat they want to select
            seat = input(
                "Enter a seat (Example: A1),"
                "or enter DONE to finish selecting: "
            ).upper()

            #Stop adding seats and move to checkout
            if seat == "DONE":
                break

            # Check that the seat has exactly one letter and one number
            if len(seat) != 2:
                print("Invalid seat selection. Try again.")
                continue

            # Separate the row letter from the seat number
            row = seat[0]
            seat_number = seat[1]

            # Check that the row and seat number are valid
            if row not in rows or seat_number not in "12345678":
                print("Invalid seat selection. Try again.")
                continue

            # Prevent customers from selecting seats already sold
            if seat in sold_seats:
                print("This seat has already been sold.")
                continue

            # Prevent customers from adding the same seat twice
            if seat in cart:
                print("This seat is already in your cart.")
                continue

            # Determine the price based on the seat selection
            if seat_number == "1" or seat_number == "8":
                price = base_price + 1
            elif seat_number == "2" or seat_number == "3":
                price = base_price - 1
            elif seat_number == "6" or seat_number == "7":
                price = base_price - 1
            else:
                price = base_price

            # Add the selected seat and its price to the cart
            cart.append(seat)
            cart_total += price

            # Show the selected seat, ticket price, and updated total
            print(f"Added seat: {seat}")
            print(f"Ticket price: ${price}")
            print(f"Updated total: ${cart_total}")

        # Checkout
        print("\n--- Checkout ---")
        print(f"Your selected seats: {cart}")
        print(f"Number of tickets: {len(cart)}")
        print(f"Total cost: ${cart_total}")

        # Give the customer the option to cancel the purchase
        if len(cart) > 0:
            decision = input(
                "Enter BUY to complete the purchase or "
                "CANCEL to empty the cart: ").upper()

            #Only mark seats as sold after the customer confirms
            if decision == "BUY":
                for seat in cart:
                    sold_seats.append(seat)

                # Add the completed purchase to total revenue
                total_revenue += cart_total
                print("Purchase completed!")

            else:
                # Discard the cart without selling the seats
                print("Purchase cancelled, your cart has been emptied.")

        else:
            print("No tickets were selected.")

        # Calculate and display the current sales stats
        seats_sold = len(sold_seats)
        percentage_sold = seats_sold / total_seats * 100

        print("\n--- Sales Summary ---")
        print(f"Seats sold: {seats_sold}")
        print(f"Percentage sold: {percentage_sold}%")
        print(f"Total revenue: ${total_revenue}")

        # The tour proceeds only if at least 50% of seats are sold
        if percentage_sold >= 50:
            print("The boat tour will proceed!")
        else:
            print("The boat tour will not proceed unless more tickets are sold.")

        # Ask whether another customer should be allowed to purchase tickets
        another_customer = input(
            "\nWould you liike to serve another customer? (YES/NO): ").upper()

        if another_customer != "YES":
            break

if __name__ == "__main__":
    main()