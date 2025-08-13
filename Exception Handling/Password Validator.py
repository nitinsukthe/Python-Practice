class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter password: ")
    if len(password) < 8 or "123" in password:
        raise WeakPasswordError("Weak password! Must be >= 8 chars and not contain '123'")
    print("Strong password.")
except WeakPasswordError as e:
    print("Error:", e)

# output:
# Enter password: Nitin@1212
# Strong password.
