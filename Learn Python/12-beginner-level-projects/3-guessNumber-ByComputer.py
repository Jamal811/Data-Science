import random 

def computer_guess(X):
    low = 1
    high = X
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # i could be high as well b/c low = high
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            
    print(f"Yay! The computer guessed the number, {guess} correctly !")
    
computer_guess(100)