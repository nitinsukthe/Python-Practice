# PASSWORD CHECKER
# Create a login system that grants access only if correct credentials are given.

correct_username = "hacker"
correct_password = "cyber123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
  print("Acess Granted. Welcome, Agent!")
else:
  print("Acess Denied. Intrusion Logged.")

# output: 
# Enter username: hacker
# Enter password: cyber123
# Acess Granted. Welcome, Agent!
