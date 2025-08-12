# How it Works
# Reads thousands of possible passwords from a file.
# Randomly chooses the “target” password.
# Brute-forces until found.
# Tracks attempts, time taken, and success rate.

# File: "wordlist.txt"
# 123456
# password
# 12345678
# qwerty
# abc123
# letmein
# admin
# root
# passw0rd
# hunter2
# dragon
# iloveyou
# monkey
# trustno1


import random
import time

def load_wordlist(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def brute_force_attack(wordlist):
    correct_password = random.choice(wordlist)
    print(f"Target password (hidden in real life!) chosen...\n")

    attempts = 0
    start_time = time.time()

    for guess in wordlist:
        attempts += 1

        if attempts % 1000 == 0:
            print(f"Attempt #{attempts}... still trying...")

        if guess == correct_password:
            end_time = time.time()
            return {
                "found": True,
                "password": guess,
                "attempts": attempts,
                "time": round(end_time - start_time, 2)
            }

    return {"found": False}

def run_tests(filename, runs=5):
    wordlist = load_wordlist(filename)
    successes = 0
    total_time = 0

    for i in range(runs):
        print(f"\n--- Test Run {i+1} ---")
        result = brute_force_attack(wordlist)
        if result["found"]:
            print(f"Password found: {result['password']}")
            print(f"Attempts: {result['attempts']}")
            print(f"Time taken: {result['time']} seconds")
            successes += 1
            total_time += result["time"]
        else:
            print("Password not found.")

    print(f"\nSuccess Rate: {(successes / runs) * 100}%")
    if successes > 0:
        print(f"Average Time: {round(total_time / successes, 2)} seconds")

run_tests("wordlist.txt", runs=3)



# output:
# --- Test Run 1 ---
# Target password (hidden in real life!) chosen...
# 
# Password found: 12345678
# Attempts: 3
# Time taken: 0.0 seconds
# 
# --- Test Run 2 ---
# Target password (hidden in real life!) chosen...
# 
# Password found: trustno1
# Attempts: 14
# Time taken: 0.0 seconds
# 
# --- Test Run 3 ---
# Target password (hidden in real life!) chosen...
# 
# Password found: root
# Attempts: 8
# Time taken: 0.0 seconds
# 
# Success Rate: 100.0%
# Average Time: 0.0 seconds
