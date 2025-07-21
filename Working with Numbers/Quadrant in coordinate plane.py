x,y=map(int,list(input("Insert the value for variable X and Y: ").split(" ")))
# First quadrant
if x>0 and y>0:
    print(f"Point ({x},{y}) lies in the First quadrant")
# Second quadrant
elif x<0 and y>0:
    print(f"Point ({x},{y}) lies in the Second quadrant")
# Thrid quadrant
elif x<0 and y<0:
    print(f"Point ({x},{y}) lies in the Thrid quadrant")
# Fourth quadrant
elif x>0 and y<0:
    print(f"Point ({x},{y}) lies in the Fourth quadrant")
# On origin
elif x==0 and y==0:
    print(f"point ({x},{y}) lies at the origin")
# On x-axis
elif x!=0 and y==0:
    print(f"Point ({x},{y}) lies on x-axis")
# On y-axis
elif x==0 and y!=0:
    print(f"Point ({x},{y}) lies on y-axis")
