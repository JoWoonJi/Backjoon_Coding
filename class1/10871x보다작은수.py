"""
n, x = map(int,input().split())
a = list(map(int,input().split()))


for i in range(n):
    if i < x:
        print(i , end=" ")
        """
"""
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=" ")
"""

n, x = map(int,input().split())
a = list(map(int,input().split()))


for i in range(n):
    if a[i] < x:
        print(a[i] , end=" ")