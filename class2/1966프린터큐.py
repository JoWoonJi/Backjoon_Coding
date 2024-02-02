from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    q = deque(enumerate(priority)) #enumerate는 (i,p)이런식으로 저장됨. 순서(인덱스)를 정해주는.
    order = 0

    while q:
        cnt = q.popleft()
        if any(cnt[1] < i[1] for i in q): #루프문과 함께하려면 any, 루프 전체를 돌면서 p값을 비교
            q.append(cnt)
        else:
            order += 1
            if cnt[0] == m:
                print(order)
                break