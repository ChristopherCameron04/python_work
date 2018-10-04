requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + " to your pizza!")
        print("\nYour order is ready for pick!")
        print("\nThank you for your business! Please come again!")
else:
    print("Are you sure you want a plain pizza?")
