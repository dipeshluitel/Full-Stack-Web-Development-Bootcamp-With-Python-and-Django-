def noTeenSum(a,b,c):
    a = fixTeen(a)
    b = fixTeen(b)
    c = fixTeen(c)
    return a+b+c

def fixTeen(num):
    if num in [13,14,17,18,19]:
        return 0;
    else:
        return num;

print(noTeenSum(2,15,16))

