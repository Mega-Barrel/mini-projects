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
    if computer_choice == 1: 
        com_cho_name = 'Rock'
    elif computer_choice == 2:
        com_cho_name = 'Paper'
    else:
        com_cho_name = 'Scissor'
    print('Computer choice is', com_cho_name)


    # Displaying user and computer choice
    print(f'user choosed {choice} and computer choosed {computer_choice}')


    # condition for winning    
    if ((choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or
    (choice == 3 and computer_choice == 2)):
        print('Player Wins')

    elif ((computer_choice == 1 and choice == 3) or (computer_choice == 2 and choice == 1) or
    (computer_choice == 3 and choice == 2)):
        print('computer Wins')
    
    elif ((choice == 1 and computer_choice == 1) or (choice == 2 and computer_choice == 2) or
    (choice == 3 and computer_choice == 3)):
        print('Both Wins')


    # To play game again or exit
    continue_game = input('Do you want to play again: ')
    if continue_game == 'no':
        print('Thank you for playing this game :)')
        break
    # if you want to play again type yes :)
    elif continue_game == 'yes':
        continue






