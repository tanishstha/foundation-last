import random

winning_number = random.randint(0,100)


def guess_function(user_provided_num):
    game_over=False
    guess_counter=1
    while not game_over:
        if winning_number==user_provided_num:
            print(f" You win the game in {guess_counter} {'time' if guess_counter==1 else 'times'} ")
            game_over=True
        else:
            if user_provided_num > winning_number:
               print("The number is too high")
            else:
               print("The number is too low")
            guess_counter += 1    
            user_provided_num = int(input("Please guess again: "))


user_provided_num = int(input("Please provide your number: "))
print(guess_function(user_provided_num))