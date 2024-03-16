import random

# a = random.random()
# print(a)
# a = random.uniform(1, 10)
# print(a)
# a = random.randint(1, 10) # upper bound means 10 is included
# print(a)
# a = random.randrange(1, 10) # upper bound means 10 is not included

# a = random.normalvariate(0, 1) # mean of zero and standard daviation of 1
# print(a)

# mylist = list("ABCDEFG")
# a = random.choice(mylist) 
# print(a)

# mylist = list("ABCDEFG")
# a = random.sample(mylist, 3) # different elements will be picked
# print(a)

# mylist = list("ABCDEFG")
# a = random.choices(mylist, k=3) # same elements can be picked
# print(a)

# mylist = list("ABCDEFG")
# random.shuffle(mylist)
# print(mylist)

# not good for security it can be guessed use secrets


# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))


# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))


# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))


# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

import secrets

# a = secrets.randbelow(10)
# print(a)

# a = secrets.randbits(4) #1111 = 15 from 0 to 15 bits
# print(a)

# mylist = list("ABCDEFG")
# a = secrets.choice(mylist) 
# print(a)

# now generate arrays randomly
import numpy as np

# a = np.random.rand(3, 3)
# print(a)

# a = np.random.randint(0, 10, 3)
# print(a)

# a = np.random.randint(0, 10, (3, 4))
# print(a)

# arr = np.array([[1, 2, 4], [4, 5, 6], [7, 8, 9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))
