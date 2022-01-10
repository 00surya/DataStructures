
def fibonacci(n):
    
    if n==0:
        return 0
    if n==1:
        return 1

    n_1 = fibonacci(n-1)
    n_2 = fibonacci(n-2)

    n = n_1+n_2


    return n

nth_fibbo = fibonacci(8)
print(nth_fibbo)

