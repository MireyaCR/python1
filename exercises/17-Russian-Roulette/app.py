import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
	aleatorio=spin_chamber()
	for i in range(aleatorio):
		if(bullet_position == i):
			return ('You are dead!')
		else:
			return('Keep playing!')
	
print(fire_gun())