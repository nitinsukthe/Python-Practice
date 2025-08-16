# * * * *  
# *       *  
# *       *  
# *       *  
# *       *  
# *       *  
# * * * *  

rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0 or \
           (i == 0 and j < cols-1) or \
           (i == rows-1 and j < cols-1) or \
           (j == cols-1 and i != 0 and i != rows-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
