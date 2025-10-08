numbers = [1,2,3,4,5,6]
numbers2 = [1,2,4,5,6]

# returns true if seqence of number 1,2,3 appears in the list

def arrayCheck(numbers):
    length = len(numbers)
    i = 0; 
    while i!=length-2:
        if((numbers[i]==1) and( numbers[i+1]==2) and numbers[i+2]==3):
             return True
        i+=1
    
    return False     

print(arrayCheck(numbers))