# def functionName(parameter1,parameter2):
#     codes here
# Filter expression

mylist = [1,2,3,4,5,6,7,8,9,10]

# def even_bool(num):
#     return num%2==0
# evens = filter(even_bool,mylist)
# print(list(evens))


# lambda expresion

# lambda num: num%2==0
evens = filter(lambda num: num%2==0,mylist)
print(list(evens))
