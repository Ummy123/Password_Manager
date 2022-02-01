__author__ = 'A. Sangha'
"""
Date: February 1, 2022
File Name: password_manager
Description: Creates a password and saves it to the computer for personal use later.
"""

import random
import pickle
import string

# Create password content
def PasswordGenerator():

    global password

    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    Numbers = string.digits
    special_characters = string.punctuation

    content = letters_lower + letters_upper + Numbers + special_characters
    length = 20
    password = ''.join(random.sample(content, length))
    return list(password)

# Save the password to the disk
def SaveList():
    pickle.dump(password, open('NewPassword', 'wb'))
    print('Password saved to disk.')

# Check to see if the password is located on the disk and allow the user to continue if it is
def PasswordCheck():
    check = True
    while check:
        User_Input = input('Please enter your password: ')
        if User_Input == pickle.load(open('NewPassword', 'rb')):
            return
        else:
            print('That is not your password!')

# Main function
def main():

    PasswordGenerator()
    print('Randomly generated password is:', password)
    SaveList()
    PasswordCheck()
    print('Program ended.')

if __name__ == '__main__':
    main()