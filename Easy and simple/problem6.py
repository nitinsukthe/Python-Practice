# Create a class "Programmer" for storing in formation of few programmers working at Microsoft

class Programmer:
  company = "Microsoft"
  def __init__(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin
    print(f"Name is {name}\nSalary is {salary}\nPin is {pin}.")

p = Programmer("Harry","1200000","1234")
print(p.company)


# output:
# Name is Harry
# Salary is 1200000
# Pin is 1234.
# Microsoft
