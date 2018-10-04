requested_toppings = ['anchovies','mushrooms', 'spinach']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("I apologize! We are out of mushrooms.")
    else:
        print("Adding " + requested_topping + " to your order.")
print("\nYour order is ready for pick up!")
print("Thank you! Please come again!")
