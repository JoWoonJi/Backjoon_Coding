import heapq
import sys
i=sys.stdin.readline
n=int(i())
h=[]
for _ in range(n):
    x=int(i())
    if x==0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,-x)