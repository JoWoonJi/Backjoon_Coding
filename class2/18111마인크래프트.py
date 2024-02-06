#간결하게
from collections import defaultdict
n, m, b = map(int, input().split())

d = defaultdict(int)
min_t, max_h = float('inf'), -1
for _ in range(n):
    for i in map(int, input().split()):
        d[i] += 1

for h in range(min(d), max(d) + 1):
    t, inv = 0, b
    for i, j in d.items():
        if h > i:
            t += (h - i) * j
            inv -= (h - i) * j
        else:
            t += 2*(i - h) * j
            inv += (i - h) * j
    if inv >= 0 and (t < min_t or (t == min_t and h > max_h)):
        min_t, max_h = t, h
print(min_t, max_h)

# # 입력값 N, M, B를 받습니다. N과 M은 지형의 크기, B는 사용할 수 있는 추가 블록의 수입니다.
# N, M, B = map(int, input().split())

# # 각 높이별로 블록의 개수를 저장할 defaultdict를 생성합니다. 기본값은 int형으로 0입니다.
# cnt = defaultdict(int)

# # N번 반복하여 각 줄의 높이 정보를 입력받고, 해당 높이의 블록 개수를 cnt에 카운트합니다.
# for _ in range(N):
#     for n in map(int, input().split()):
#         cnt[n] += 1

# # 결과를 저장할 변수들을 초기화합니다. min_time은 최소 시간, max_height는 그 때의 높이입니다.
# min_time, max_height = float('inf'), -1

# # 가능한 모든 높이 h에 대해 반복문을 실행합니다. min(cnt)에서 max(cnt)+1까지입니다.
# for h in range(min(cnt), max(cnt)+1):
#     time, inv = 0, B  # time은 필요한 시간, inv는 조정 후 남은 블록의 수입니다.

#     # cnt의 각 항목(높이 k와 그 높이의 블록 수 v)에 대해 반복합니다.
#     for k, v in cnt.items():
#         if h > k:  # 목표 높이 h가 현재 높이 k보다 높으면, v개의 블록을 추가해야 합니다.
#             time += (h - k) * v  # 블록을 추가하는 데 필요한 시간을 time에 더합니다.
#             inv -= (h - k) * v  # 추가한 블록 수만큼 inv에서 빼줍니다.
#         else:  # 목표 높이 h가 현재 높이 k보다 낮으면, v개의 블록을 제거해야 합니다.
#             time += 2 * (k - h) * v  # 블록을 제거하는 데 필요한 시간(2배)을 time에 더합니다.
#             inv += (k - h) * v  # 제거한 블록 수만큼 inv에 더합니다.

#     # 모든 조정이 완료된 후 inv가 0 이상이고, 계산된 시간이 현재 최소 시간보다 작거나 같으면 결과를 업데이트합니다.
#     if inv >= 0 and (time < min_time or (time == min_time and h > max_height)):
#         min_time, max_height = time, h  # 최소 시간과 그 때의 높이를 업데이트합니다.

# # 최종적으로 계산된 최소 시간과 그 때의 높이를 출력합니다.
# print(min_time, max_height)
