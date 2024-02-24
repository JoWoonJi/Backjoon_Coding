import sys # from collections import deque를 사용하면 pop(0)대신 popleft를 쓰는데, pop은 앞에 없애면 한칸씩 당겨야해서 연산이 더 오래걸리고, 디큐는 이중연결리스트라 양끝을 뺄때는 하나씩 당기지 않는다고 한다.

n = int(input())
q = []

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    cmd = command[0]

    if cmd == 'push':
        q.append(command[1])
    if cmd == 'pop':
        print(q.pop(0) if q else -1) #스택과 큐의 차이. 스택은 마지막꺼() 빼고 큐는 처음꺼(0) 빼고 
    if cmd == 'size':
        print(len(q))
    if cmd == 'empty':
        print(1 if not q else 0)
    if cmd == 'front':
        print(q[0] if q else -1)
    if cmd == 'back':
        print(q[-1] if q else -1)