# System will generate a random password from a given list.
# You must brute-force it by checking each guess.
# Track how many attempts and how long it takes.

import random
import time

password_list = ["admin", "root", "letmein", "123456", "dragon", "hunter2", "passw0rd", "qwerty"]

correct_password = random.choice(password_list)

print("Starting password brute-force simulation...\n")

start_time = time.time()

attempts = 0
for guess in password_list:
    attempts += 1
    print(f"Trying password: {guess}")
    time.sleep(0.5)  # slow down for realism

    if guess == correct_password:
        end_time = time.time()
        print(f"\nPassword found: {guess}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {round(end_time - start_time, 2)} seconds")
        break
else:
    print("\nNo password match found.")


# output:
# Starting password brute-force simulation...

# Trying password: admin
# Trying password: root
# Trying password: letmein

# Password found: letmein
# Attempts: 3
# Time taken: 1.5 seconds
