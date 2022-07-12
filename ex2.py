def fib(k):
    if k == 1:
        return 1
    elif k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)    

def fib_sequence_contains(x):
    y = 0
    k = 1

    while y < x:
        y = fib(k)
        k = k + 1

    return y == x

x = int(input())
print(fib_sequence_contains(x))    