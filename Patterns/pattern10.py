  # * * * * 
# *         
# *         
# *         
# *         
# *         
  # * * * * 

rows = 7
cols = 5

for i in range(rows):
    for j in range(cols):
        if (i == 0 and j > 0) or \
           (i == rows-1 and j > 0) or \
           (j == 0 and i != 0 and i != rows-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
