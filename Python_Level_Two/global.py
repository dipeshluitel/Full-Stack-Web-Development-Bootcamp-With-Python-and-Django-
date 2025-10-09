# this is local value

x=500

def globalValue():
    global x
    x=1000

print(f"Before function call x= {x}")
globalValue()
print(f"After function call x= {x}")
