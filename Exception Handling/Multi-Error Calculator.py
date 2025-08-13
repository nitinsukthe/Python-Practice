try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        raise ValueError("Invalid operation!")

except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")
except ValueError as e:
    print("❌ Error:", e)

# output:
# Enter first number: 2
# Enter second number: 4
# Enter operation (+, -, *, /): +
# Result: 6.0
