# is_male = True

# if is_male:
#     print("you are a male")

# is_male = False

# if is_male:
#     print("you are a male")
# else:
#     print("You are not a male")


# is_male = True
# is_tall = True

# if is_male or is_tall:
#     print("you are a male or tall or both")
# else:
#     print("You are neither a male nor tall")
    
# is_male = True
# is_tall = False

# if is_male and  is_tall:
#     print("you are a tall male")
# else:
#     print("You are eaither not male or tall or both")

is_male = False
is_tall = False

if is_male and  is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but you are tall")
else:
    print("You are not a man and not tall")


