String=input("Enter the String: ")
String=String[0:1].upper()+String[1:len(String)-1]+String[len(String)-1:len(String)].upper()
print(String)
