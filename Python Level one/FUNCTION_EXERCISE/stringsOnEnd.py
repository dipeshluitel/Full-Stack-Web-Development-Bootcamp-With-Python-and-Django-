str1 = input("Enter the first string: ").lower()
str2 = input("Enter the Second string: ").lower()

def endOther(str1,str2):
    str1_list = list(str1)
    str2_list = list(str2)
    if((str1_list == str2_list[len(str2)-len(str1):] )or (str2_list == str1_list[len(str1)-len(str2):])):
        return True
    
print(endOther(str1,str2))
