# *           * 
# * *         * 
# *   *       * 
# *     *     * 
# *       *   * 
# *         * * 
# *           * 

rows = 7
cols = 7 

for i in range(rows):
    for j in range(cols):
        if j == 0 or j == cols-1:
            print("*", end=" ")
        elif i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
