''' QUESTION 8'''

# Aprogram that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.


import random
number = bin(random.randint(1000,9999))
print(int(number, 2))


#