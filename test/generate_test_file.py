# Generate a file made up of random integers

import numpy as np

quantity = int(input("How many? "))
limit = int(input("Max integer: "))
filename = "numbers.txt"

numbers = np.random.randint(low=0, high=limit+1, size=quantity)

f = open(filename, 'w')
for n in numbers:
    f.write("{}\n".format(n))

