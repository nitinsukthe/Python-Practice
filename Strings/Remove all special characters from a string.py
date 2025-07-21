string1="PreP!@#insta"
string2=''
for i in string1:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        string2+=i
print(f"Alphabets in string are: {string2}")
