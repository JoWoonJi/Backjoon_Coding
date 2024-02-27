#간결하게
import sys
i=sys.stdin.readline
import heapq
n=int(i())
h=[]
for _ in range(n):
    x=int(i())
    if x==0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,x)

# import heapq
# import sys
# i=sys.stdin.readline
# o=sys.stdout.write
# def m(n):
#     h=[]
#     r=[]
#     for _ in range(n):
#         x=int(i())
#         if x==0:
#             if h:
#                 r.append(str(heapq.heappop(h)))
#             else:
#                 r.append('0')
#         else:
#             heapq.heappush(h,x)
#     return r
# n=int(i())
# r=m(n)
# o('\n'.join(r))

#pypy3로하면 되고 그냥 하면 시간초과
# import heapq

# def min_heap_operations(n):
#     heap = [] 
#     results = []

#     for _ in range(n):
#         op = int(input()) 
#         if op == 0: 
#             if heap: 
#                 results.append(heapq.heappop(heap)) 
#             else: 
#                 results.append(0) 
#         else: 
#             heapq.heappush(heap, op) 

#     return results


# n = int(input())

# results = min_heap_operations(n)
# for result in results:
#     print(result)

