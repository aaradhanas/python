# Prompting for user input, while loop

prompt = "\nEnter a city that you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I would love to go to "+ city.title())

