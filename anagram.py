'''
Project 5 : Anagram 

Make a anagram validator.
Enter a string and check if the string is anagram or not. 

If the string is not anagram print("Not a anagram")

If the string is anagram print("Anagram")
''' 

# a = input('Enter 1st sentence or integer: ')
# b = input('Enter 2nd sentence or integer: ')

while True:
    def anagram_checker():
        a = input('Enter 1st sentence or integer: ')
        b = input('Enter 2nd sentence or integer: ')
        if sorted(a) == sorted(b):
            print('<-Anagram->')
        else:
            print('<-Not a Anagram->')

    
    play_again = input('Do you want to play Anagram Checker: ')
    if play_again == 'no':
        print('Thank you for playing Anagram checker :)')
        break
    elif play_again == 'yes':
        anagram_checker()

