import random

# your code here
def generate_random():
  	# CHANGE ONLY THIS LINE BELOW
	random_number = random.randint(0,9)
	return int(random_number)

print(generate_random())