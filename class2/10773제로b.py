import sys
k = int(input())
stack = []
for _ in range(k):
    n = int(sys.stdin.readline().strip())
    if n != 0:
        stack.append(n)
    if n == 0:
        stack.pop()
print(sum(stack))