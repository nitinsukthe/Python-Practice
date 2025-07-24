#    1
#   111
#  11111
# 1111111
#111111111

n = 5
for i in range(n):
    spaces = " " * (n - i - 1)
    ones = "1" * (2 * i + 1)
    print(spaces + ones)
