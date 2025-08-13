try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number!")
else:
    print("Valid number:", num)
finally:
    print("Process completed.")

# output:
# Enter a number: 12
# Valid number: 12
# Process completed.
