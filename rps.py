import random

def start(win_count, loss_count):
    print("Choose Rock, Paper, or Scissors")
    user_throw = input()
    play_rps(user_throw, win_count, loss_count)

def victory(win_count, loss_count):
     print(f"You won!")
     win_count += 1
     play_again(win_count, loss_count)

def loss(win_count, loss_count):
    print(f"You lost!")
    loss_count += 1
    play_again(win_count, loss_count)

def play_again(win_count, loss_count):
    print(f"Hit y to play again or hit any other key to quit" )
    play_bool = input()
    if play_bool != "y":
        print(f"You won {win_count} times and lost {loss_count} times")
    else:
        start(win_count, loss_count)


def play_rps(user_throw, win_count, loss_count):
    computer_possibilities = ["Rock", "Paper", "Scissors"] 
    index = random.randint(0,2)
    if (user_throw != "Rock" and user_throw != "Paper" and user_throw !="Scissors"):
        print("Not a valid  selection, please try again")
        start(win_count, loss_count)
    else:
        print(f"You played {user_throw} and the computer played {computer_possibilities[index]}")
        if(user_throw == computer_possibilities[index]):
              print(f"You tied, try again")
              start(win_count, loss_count)
        elif(user_throw == "Paper" and computer_possibilities[index] == "Rock" or user_throw == "Scissors" and computer_possibilities[index] == "Paper" or user_throw == "Rock" and computer_possibilities[index] == "Scissors"):
            victory(win_count, loss_count)
        else:
            loss(win_count, loss_count)  
             
                               

start(0, 0)