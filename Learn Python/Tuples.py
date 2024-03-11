# Tuple a type of data structure, a structure of container to store different pieces of information, It is immutable that means that it can't be changed or modified.

coordinates_tuple = (4, 5)
#coordinates_tuple[0] = 2
print(coordinates_tuple[0])

#difference between lists and tuples

coordinates_list = [4, 5]
coordinates_list[0] = 2
print(coordinates_list[0])

#you can store tupples inside lists

list_of_tupples = [(2 ,4), (5, 7)]
print(list_of_tupples[0][0])
