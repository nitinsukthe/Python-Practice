# Q2 Write a program to fill in a letter template given below with name and date.
# Dear <|Name|>,
# You are selected!
# <|Date|>

letter = '''Dear <|Name|>,
Yor are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Nitin").replace("<|Date|>","24 sep 2050"))
# Expected output: 
# Dear Nitin,
# Yor are selected!
# 24 sep 2050
