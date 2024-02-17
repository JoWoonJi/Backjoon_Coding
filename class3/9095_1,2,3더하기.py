#간결하게
def c(n):
    if n<0:
        return 0
    if n == 0:
        return 1
    return c(n-1) + c(n-2) + c(n-3)
t= int(input())
r=[]
for _ in range(t):
    n = int(input())
    r.append(c(n))
for i in r:
    print(i)

# def count_ways(n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
    
#     return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

# T = int(input()) 
# results = []

# for _ in range(T):
#     n = int(input()) 
#     results.append(count_ways(n))

# for result in results:
#     print(result)
