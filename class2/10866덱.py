import sys
from collections import deque

n = int(input())

deck = deque() #[]하면 appendleft 사용불가능

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    cmd = command[0]

    if cmd == 'push_front':
        deck.appendleft(command[1])
    elif cmd == 'push_back':
        deck.append(command[1])
    elif cmd == 'pop_front':
        print(deck.popleft() if deck else -1)
    elif cmd == 'pop_back':
        print(deck.pop() if deck else -1)
    elif cmd == 'size':
        print(len(deck))
    elif cmd == 'empty':
        print(1 if not deck else 0)
    elif cmd == 'front':
        print(deck[0] if deck else -1)
    elif cmd == 'back':
        print(deck[-1] if deck else -1)
