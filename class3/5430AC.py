from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    array = input().rstrip()[1:-1].split(",")

    dq = deque(array) if n > 0 else deque()

    is_reversed = False
    is_error = False

    for op in p:
        if op == 'R':
            is_reversed = not is_reversed
        elif op == 'D':
            if dq:
                if is_reversed:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                is_error = True
                break

    if is_error:
        print("error")
    else:
        if is_reversed:
            dq.reverse()
        print("[" + ",".join(dq) + "]")