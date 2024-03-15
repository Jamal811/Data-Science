import random

def play():
    user = input("Whats you choise? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'tie'
        
    if is_win(user, computer):
        return 'You won!'
    
    return 'You Lost'
        
def is_win(player, openent):
    #r > s, s > p, p > r
    if(player == 'r' and openent == 's') or (player == 's' and openent == 'p') or (player == 'p' and openent == 'r'):
        return True
    
print(play())