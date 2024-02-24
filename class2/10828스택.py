import sys #첫시도에 그냥 하니 시간 초과됨.

n = int(input())
stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    print(1 if not stack else 0)

def top():
    print(stack[-1] if stack else -1)

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    cmd = command[0]

    if cmd == "push":
        push(int(command[1]))
    elif cmd == "pop":
        pop()
    elif cmd == "size":
        size()
    elif cmd == "empty":
        empty()
    elif cmd == "top":
        top()

# //
        
# 함수 없이 간결하게
# import sys

# n = int(input())
# stack = []

# for _ in range(n):
#     command = sys.stdin.readline().strip().split()
#     cmd = command[0]

#     if cmd == 'push':
#         stack.append(command[1])
#     elif cmd == 'pop':
#         print(stack.pop() if stack else -1)
#     elif cmd == 'size':
#         print(len(stack))
#     elif cmd == 'empty':
#         print(1 if not stack else 0)
#     elif cmd == 'top':
#         print(stack[-1] if stack else -1)