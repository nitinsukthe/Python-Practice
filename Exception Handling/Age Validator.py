try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Age accepted")
except ValueError as e:
    print("Error:", e)

# output:
# Enter your age: 20
# Age accepted
