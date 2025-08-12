# PASSWORD STRENGTH CHECKER

import string

def check_password_strength(password):
    special_symbols = string.punctuation
    is_long_enough = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in special_symbols for char in password)
    feedback = []
    if is_long_enough and has_digit and has_symbol:
        feedback.append("Excellent! Your password meets all the strength requirements.")
    else:
        feedback.append("Your password could be stronger. Here's what's missing:")
        if not is_long_enough:
            feedback.append("  - It must be at least 8 characters long.")
        if not has_digit:
            feedback.append("  - It must contain at least one number.")
        if not has_symbol:
            feedback.append("  - It must contain at least one special symbol.")
    for line in feedback:
        print(line)
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    check_password_strength(user_password)

# output:
# Enter a password to check its strength: nitin@12
# Excellent! Your password meets all the strength requirements.
