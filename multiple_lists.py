available_toppings = ['mushrooms', 'spinach', 'olives', 'pinapple',
                    'tofu', 'yellow peppers', 'green peppers', 
                    'extra vegan cheese']
requested_toppings = ['mushrooms', 'slaw', 'extra vegan cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("I apologize! We don't have " + requested_topping + ".")
    
print("\nYour order is ready for pick up!")
print("\nThank you for your business! Please come again!")
