import random
a=0
b=random.randint(1,9)
try:
    c=b/a
    
except IOError: # we can assign different exception particularly too like(ZeroDivisionError, IndexError, IOError,etc)
    print("WELL WELL WELL I cannot open file")

except ZeroDivisionError:
    print("I cannot divide by zero")

#except:
#codes here( We can use except in this way too)
else:
    print(f"The Result is {c}")