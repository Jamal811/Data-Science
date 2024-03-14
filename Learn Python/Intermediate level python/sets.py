# collection datatype unorderd and mutable unlike lista and tupples it does not allowed duplicates
# no key value pair. just sinple elements seperated by a comma\
    
# myset = {1, 2, 3}
# print(myset)

# myset = set([1,2,4, 2]) #lists inside set
# print(myset)

# myset = set("Hello") 
# print(myset)

# myset = {} # bahave like dictionary actually it is dictionary now, use set keyword if you want an empty set
# print(type(myset))

# myset = set()
# print(type(myset))

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset.add(4)

# myset.remove(2)
# myset.discard(3)
# myset.pop() #remove 1

# print(myset)

# myset = {1, 3, 2, 5}
# for i in myset:
#     print(i)
# if 4 in myset:
#     print("yes")
# else:
#     print("No")

# Unions and intersections

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)

# e = evens.intersection(primes)
# print(e)

# difference

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)
# print(diff)

# diff = setB.difference(setA)
# print(diff)

# diff = setB.symmetric_difference(setA)
# print(diff)

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
print(setB.issuperset(setA))








