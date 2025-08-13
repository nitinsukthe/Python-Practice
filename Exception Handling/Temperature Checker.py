try:
    temp = float(input("Enter temperature: "))
    if temp < -50 or temp > 60:
        raise ValueError("Temperature out of range!")
    print("Temperature is within range.")
except ValueError as e:
    print("Error:", e)

# output:
# Enter temperature: 20
# Temperature is within range.
