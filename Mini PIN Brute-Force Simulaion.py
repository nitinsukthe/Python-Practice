# Program generates a random “PIN” (4 digits).
# You write a loop to “brute-force” it — try every combination until correct.
# Count how many attempts it took.

import random
import time

def brute_force_pin_simulation():
    """
    Simulates a brute-force attack to guess a 4-digit PIN.
    The program generates a random PIN and then iterates through every
    possible combination from '0000' to '9999' until it finds the correct one.
    """
    secret_pin = f"{random.randint(0, 9999):04d}"

    print("Initiating PIN brute-force simulation...")
    print(f"Target PIN has been generated: {secret_pin}")
    print("Brute-forcing... this may take a moment.")
    print("-" * 30)

    attempts = 0
    start_time = time.time()

    for i in range(10000):
        attempt_pin = f"{i:04d}"
        attempts += 1

        if attempt_pin == secret_pin:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"\nSUCCESS! The PIN was cracked.")
            print(f"Correct PIN: {secret_pin}")
            print(f"Attempts taken: {attempts}")
            print(f"Time elapsed: {elapsed_time:.4f} seconds")
            break

if __name__ == "__main__":
    brute_force_pin_simulation()


# output:
# Initiating PIN brute-force simulation...
# Target PIN has been generated: 9587
# Brute-forcing... this may take a moment.
# ------------------------------

# SUCCESS! The PIN was cracked.
# Correct PIN: 9587
# Attempts taken: 9588
# Time elapsed: 0.0027 seconds
