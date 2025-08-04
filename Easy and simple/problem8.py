# Write a python function which converts inches to cms.

def inch_to_cms(inch):
  return inch*2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


# # output:
# Enter value in inches: 7
# The corresponding value in cms is 17.78
