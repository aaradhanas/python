# Specify an object structure like a map and access it using a key

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'slow'}
print("Original position is "+ str(alien_0['x_position']))

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position']+ x_increment;
print("New position is "+ str(alien_0['x_position'])) 

