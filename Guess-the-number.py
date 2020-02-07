'''
This project also uses the random module in Python. 
The program will first randomly generate a number unknown to the user. 
The user needs to guess what that number is. (In other words, the user needs to be able to input information.) 
If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high 
or too low). If the user guesses correctly, a positive indication should appear. 
You’ll need functions to check if the user input is an actual number, 
to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.


1. Random function
2. Variables
3. Integers
4. Input/Output
5. Print
6. If/Else statements

'''
import random

number = random.randint(1, 10)
guess = int(input('enter a number: '))


def difference():
    answer = guess - number
    print(f'The difference is {answer}')
    return answer

if guess == number:
    print('You guessed the number correctly')
    difference()    
            
elif guess > number:
    print('The guessed number is higher')
    print('You should haved guessed lower number')
    difference()

else:
    print('The guessed number is lower')
    print('You should have guessed higher number')
    difference()  

print('Thank you For playing Guess-The-Number Game :)')
   
