# Random module - make easy to generate random numbers

import random
import my_module # another python file imported

# take help of askpython website
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random() # generates random floating point number between 0 to 1
print(random_float)

random_float * 5 # generates random floating point number between 0 - 5, by just multiplying previous variable by 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")