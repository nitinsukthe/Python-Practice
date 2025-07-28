# Q3 A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

comments = ["Make a lot of money", "buy now", "subscribe this", "click this"]
message = input("Enter your message: ")
if message in comments:
  print("This comment is a spam.")
else:
  print("This comment is not a spam.")

# output: Enter your message: buy now
#         This comment is a spam.
