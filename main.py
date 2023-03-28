import random
print("welcome to the rock,paper,scissors")
while True:
    options=['rock','paper','scissors']
    comp_choice = random.choice(options)
    user_choice = input("enter rock, paper or scissors:")
    user_choice = user_choice.lower()
    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        user_choice = input("enter rock, paper or scissors:")
    print(f'computer chose {comp_choice}')
    if user_choice == comp_choice:
        print('It was a tie')
    elif user_choice == "rock" and comp_choice == 'paper':
        print('computer wins this round!')
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print('You win this round!')
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('You win this round!')
    elif user_choice == 'paper' and comp_choice == 'scissors':
        print('Computer wins this round!')
    elif user_choice == 'scissors' and comp_choice == 'rock':
        print('Computer wins this round!')
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('You win this round!')
    again=input('would you like to go again Y/N')
    again = again.lower()
    if again != 'yes' and again !='y':
        break