def factorial1(a):    
    if a<=1 : 
        return 1
    return a * factorial1(a-1)

def factorial2(a, b):    
    if a<=b : 
        return 1
    return a * factorial2(a-1, b)

n, k = map(int, input().split())
print(factorial2(n,k) // (factorial1(n-k)) )
exit(0)