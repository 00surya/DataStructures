import math 
def merge_short(a,lb,ub):
    if lb<ub:
        mid = (lb+ub)//2
        print(mid)
        merge_short(a,lb,mid)
        print("hello")
        merge_short(a,mid+1,ub)
        merge(a,lb,mid,ub)

def merge(a,lb,mid,ub):
    pass

df = merge_short([3,2,1],0,8)
print(df)
print("......\n\n\n\n")


def merge_first(a):
    if a==0:
        return a
    else:
        return a+merge_first(a-1)
w = merge_first(2)
print(w)



def factorial_recursive(n):

    if n ==1:
        print("returning 1.....")
        return 1
    else:
        print(n)
        a = n*factorial_recursive(n-1) # memory stackk
        return a

# 5 * facotorial_recursive(4)
# 5 * (> 4 * facotorial_recursive(3) ) 
# 5 * 4 * (> 3 * facotorial_recursive(2) )
# 5 * 4 * 3 * (> 2 * facotorial_recursive(1) )
# 5 * 4 * 3 * 2 * (> 1 ) 

df = factorial_recursive(9)

print(type(df))

print(f":)\nresult>\n{df}")


def d(l):  
    if l ==1:
        return "1"
    else:
        return "s>"+d(l-1)    


x = d(3)        

print(x)