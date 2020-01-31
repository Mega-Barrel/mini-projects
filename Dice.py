'''
Project 1 : Dice simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling
dice. 
When the program runs, it will randomly choose a number between 1 and 6.
The program will print what that number is. It should then ask you if you’d like to roll again. 
For this project, you’ll need to set the min and max number that your dice can produce. 
For the average die, that means a minimum of 1 and a maximum of 6. 
You’ll also want a function that randomly grabs a number within that range and prints it.


1. Random
2. Integer
3. Print
'''

import random

min = 1
max = 6

def dice():
    for i in range(1, 6):
        answer = random.randint(min, max)
        print(f'The dice has rolled {answer}')        
        print('Would you want to roll the dice again ? ')
        word = input('Enter y for yes and n for no: ')
        if word == 'y':
            for i in range(1, 6):
                answer = random.randint(min, max)
                break
                print(f'The dice has rolled {answer}')
                # break
        else:
            print('thank you for playing Dice Simulator, see you next time')
            break
    return answer
dice()

















