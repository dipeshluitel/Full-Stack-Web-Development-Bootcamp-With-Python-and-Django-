def dblStr(str):
    newStr = ""
    for i in range(len(str)):
        newStr+=str[i]*2
    print(f"After Doubling: {newStr}")

str=input("Enter the string: ")
dblStr(str)