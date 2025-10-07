#operators (comparision and logical)

# greater than (a>b)
# less than (a<b)
# greater than or equal (a>=b)
# less than or equal (a>=b)

#Equality

1==1
1=="1"
print(1=="1")

#logical

print((1>2) and (1<2))
print((1>2) or (1<2))

#if-elif-else

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
