num1, num2, num3 = 10,20,30
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)
                   OR          
num1, num2, num3 = 10,20,30
print(max(num1, num2, num3))
