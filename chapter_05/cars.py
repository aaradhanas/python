# else statement in if clause, string's upper() method

cars = ['audi', 'bmw', 'jaguar']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())