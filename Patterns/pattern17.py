# * * * * * 
#     *     
#     *     
#     *     
#     *     
# *   *     
#   *       

rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0:
            print("*", end=" ")
        elif j == cols//2 and i != rows-1:
            print("*", end=" ")
        elif i == rows-1 and j < cols//2 and j > 0:
            print("*", end=" ")
        elif i == rows-2 and j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
