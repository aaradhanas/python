# Create an empty list for storing aliens.
aliens = []

# Create 30 green aliens.
for alien_num in range(0,30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#First 3 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Print the first 5 aliens
for alien in aliens[0:5]:
    print(alien)


