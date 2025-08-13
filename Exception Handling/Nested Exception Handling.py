try:
    num = int(input("Enter a number to divide 100: "))
    result = 100 / num

    try:
        with open("log.txt", "w") as f:
            f.write(f"Result is {result}")
        print("Result written to file.")
    except IOError:
        print("File writing error!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

# output:
# Enter a number to divide 100: 100
# Result written to file.
