my_foods = ['Salmon', 'Sardines', 'Peanut Butter','Spinach', 'Smoothies', 'Green Apples']
friend_foods = my_foods[:]

my_foods.append('avocado')
friend_foods.append('red apples')

for food in my_foods:
	print(food)

for food in friend_foods:
	print(food)
