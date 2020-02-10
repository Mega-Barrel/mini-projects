'''
Project 3: Mad Libs Generator

The Goal: 
The program will first prompt the user for a series of inputs a la Mad Libs. 
For example, a singular noun, an adjective, etc. 
Then, once all the information has been inputted, the program will take that data and place them 
into a premade story template. You’ll need prompts for user input,
and to then print out the full story at the end with the input included.

Concepts to keep in mind:

1. Strings
2. Variables
3. Concatenation
4. Print

'''
noun = input('Enter a noun: ')
plural_noun = input('Enter a plural noun: ')
verb = input('Enter a verb(present tense): ')
verb1 = input('Enter a verb(present tense): ')

print('Today, every student has a computer small enough to fit into his', noun, '.')
print('He can solve any math problem by simply pushing the computers little', plural_noun, '.')
print('Computer can add, multiply, divide, and', verb, '.')
print('They can also', verb1,'better than a human.')







