empty_line = "\n"

# Empty list to store all of aliens created.
aliens = []

# Makes 30 aliens. Range tells how many types to repeat loop.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
#Shows he first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
    

print(empty_line)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print(alien)
print("...")

print(empty_line)
        
for alien in aliens[0:3]:
       if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        print(alien)
print("...")

# Shows how many aliens have been created.
print("\nTotal number of aliens: " + str(len(aliens)))
