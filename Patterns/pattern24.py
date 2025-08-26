#   * * *   
# *       * 
# *       * 
# *     * * 
# *       * 
#   * * *   
# *       * 

rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if (i == 0 or i == rows-2) and (j != 0 and j != cols-1):
            print("*", end=" ")
        elif (j == 0 or j == cols-1) and (i != 0 and i != rows-2):
            print("*", end=" ")
        elif i == j and i >= rows//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
