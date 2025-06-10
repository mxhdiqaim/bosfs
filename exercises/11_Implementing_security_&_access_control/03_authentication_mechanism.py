# Implement a simple two-factor authentication system that requires a password and a verification code.

import random

def two_factor_authentication_system():
    # Preset correct password for demonstration
    correct_password = 'securePass123'
    
    # Simulate user password input
    password = input('Enter your password: ')

    # Check if the entered password matches
    if password == correct_password:
        # Generate a random 6-digit verification code
        verification_code = random.randint(100000, 999999)
        print(f'Verification code sent to your phone: {verification_code}')

        # Simulate user entering the verification code
        user_code = int(input('Enter the verification code: '))

        # Check if the code matches
        if user_code == verification_code:
            print('Authentication successful!')
        else:
            print('Incorrect verification code. Authentication failed.')
    else:
        print('Incorrect password. Authentication failed.')


# Example Usage
two_factor_authentication_system()

"""
Explanation
This code implements a simple two-factor authentication system

It prompts the user for a password and validates it

If correct, it simulates sending a random 6-digit verification code to the user's phone

The user must then enter this code to complete the authentication process

This demonstrates the added security of multi-factor authentication by requiring something you know (password) and something you have (verification code).
"""