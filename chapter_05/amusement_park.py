# Conditional statements - if/elif

age = 12

if age < 6:
    price  = 0
elif age < 12:
    price = 10
elif age < 18:
    price = 15

#And integer value needs to be cast to a string before appending to another string
print("Your admission cost is $"+ str(price))