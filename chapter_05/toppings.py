# "in" is used as a contains


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+ requested_topping)
    else:
        print("Sorry, couldn't add "+ requested_topping)

print("\nFinished making your pizza")