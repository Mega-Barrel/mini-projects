'''
Project 4 : Rock, Paper, Scissors Game

Make a rock-paper-scissors game where it is the player vs the computer. 
The computer’s answer will be randomly generated, while the program will ask
the user for their input. 
This project will better your understanding of while loops and if statements.

''' 
import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n") 

while True:
    # For user to choose an input
    print('Enter choice \n 1.Rock \n 2.Paper \n 3.Scissor')
    choice = int(input('Enter choice from 1 to 3: '))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    print('User choice is', choice_name)
    
    # For computer to randomly generate a value
    computer_choice = random.randint(1,3)
    # while computer_choice == choice:
    if computer_choice == 1: 
        com_cho_name = 'Rock'
    elif computer_choice == 2:
        com_cho_name = 'Paper'
    else:
        com_cho_name = 'Scissor'
    print('Computer choice is', com_cho_name)

    # condition for winning
    print(f'user chosed {choice} and computer {computer_choice}')
    if (choice == 1 and computer_choice == 3):
        print('user Wins')
        result = 'Rock'
    elif (choice == 3 and computer_choice == 2):
        print('computer Wins')
        result = 'Scissor'
    elif (choice == 3 and computer_choice == 1):
        print('computer Wins')
        result = 'Paper'

print()
# print(random1)





