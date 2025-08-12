# SIMPLE TEXT MENU

import datetime

def display_menu():
    menu = """
1. Say Hello
2. Show Current Year
3. Exit
"""
    print(menu)

def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("\nHello!\n")
        elif choice == '2':
            current_year = datetime.datetime.now().year
            print(f"\nThe current year is: {current_year}\n")
        elif choice == '3':
            print("\nExiting the program. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")

run_menu()

# output:
# 1. Say Hello
# 2. Show Current Year
# 3. Exit

# Enter your choice (1, 2, or 3): 1
# Hello!
# 1. Say Hello
# 2. Show Current Year
# 3. Exit

# Enter your choice (1, 2, or 3): 2
# The current year is: 2025
# 1. Say Hello
# 2. Show Current Year
# 3. Exit

# Enter your choice (1, 2, or 3): 3
# Exiting the program. Goodbye!
