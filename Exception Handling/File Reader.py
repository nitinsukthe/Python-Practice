try:
    with open("myfile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# output:
# File not found!
