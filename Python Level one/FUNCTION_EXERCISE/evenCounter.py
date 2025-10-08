numbers = [1,2,3,4,5,6,7,8,9,10]


def countEvens(numbers):
    evens=[]
    for num in numbers:
        if num%2 == 0:
            evens.append(num)
    return len(evens)      

print(countEvens(numbers))