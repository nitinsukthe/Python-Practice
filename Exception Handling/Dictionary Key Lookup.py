fruits = {"apple": 50, "banana": 20, "mango": 100}

try:
    fruit = input("Enter fruit name: ").lower()
    print(f"Price of {fruit}: {fruits[fruit]}")
except KeyError:
    print("Fruit not found in list!")

# output:
# Enter fruit name: apple
# Price of apple: 50
