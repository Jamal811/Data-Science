#wount work 
def cube(num):
    num*num*num

cube(3)
print(cube(3))

#will work
def cube(num):
    return num*num*num
    print("h1") #will never runs this after return statement

cube(3)
print(cube(3))

# same
def cube(num):
    return num*num*num
    print("h1") 

result = cube(3)
print(result)
    