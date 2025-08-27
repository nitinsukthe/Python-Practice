# * * * *
# *       *
# *       *
# * * * *
# *   *
# *     *
# *       *

rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0:
            print("*", end=" ")
        elif i == 0 and j < cols-1:
            print("*", end=" ")
        elif i == rows//2 and j < cols-1:
            print("*", end=" ")
        elif j == cols-1 and i > 0 and i < rows//2:
            print("*", end=" ")
        elif i - j == rows//2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
