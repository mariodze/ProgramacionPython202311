
### 100 + 99 + 98 +2 + .. 1(ultimo ejecutar)
def sumRecursiva(n:int)->int:
    if n==1:
        return 1
    else:
        return n+sumRecursiva(n-1)
    # n + n-1 + n-2+ .......+1
    # n=100

def sumRecursivaV2(n:int)->int:
    if n!=1:
        return n+sumRecursiva(n-1)
    return 1


#factorial 5*4*3*2*1

def factorial(n:int)->int:
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1
    

print(sumRecursiva(100),'=>',sumRecursivaV2(100),"=>",factorial(5))