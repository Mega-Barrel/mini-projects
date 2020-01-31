'''
writing a program that simulates rolling dice.
When the program runs, it will randomly choose a number between 1 and 6.
The program will print what that number is.
It should then ask you if you’d like to roll again.
you’ll need to set the min and max number that your dice can produce. 
For the average die, that means a minimum of 1 and a maximum of 6. 
You’ll also want a function that randomly grabs a number within that range and prints it.


1. Random
2. Integer
3. Print
4. While Loops
'''

import random 
min = 1
max = 6
letter = True

def dice():    
    while True:
        for i in range(1, 6):
            answer = random.randint(min, max)
            break    
        print(f'Your Dice has rolled up {answer}')

        print('do you want to roll the dice again: ')
        letter = input('enter yes or no : ')
        if letter == 'y':
            for i in range(1, 6):
                answer = random.randint(min, max)   
                break   
                print(f'Your Dice has rolled up {answer}')
        else:
            break
       
    return answer
dice()

               
                
        
    











