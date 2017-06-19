pizza = {
    'crust' : 'thin',
    'toppings' : ['mushroom', 'jalepenos']
}

#Summarize the order
print("You ordered a "+ pizza['crust'] +"-crust pizza with the following toppings : ")

for topping in pizza['toppings']:
    print("\t"+topping)