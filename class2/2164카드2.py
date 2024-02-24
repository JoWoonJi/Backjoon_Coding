#같은 로직인데 list대신 deque를 활용해서 빠르게 처리하는 방법
from collections import deque

n = int(input())
deck = deque(range(1, n + 1))

while len(deck) > 1:
    deck.popleft()  
    deck.append(deck.popleft())

print(deck[0]) #그냥 deck 출력하면 deque([4]) 이런식으로 출력되어서 틀리게 된다.
# deque(더블 엔드 큐)를 사용하면 이 코드가 더 빨라지는 이유는 deque의 내부 구현 방식 때문입니다.
# deque는 양쪽 끝에서 요소를 추가하거나 제거하는 연산을 매우 효율적으로 수행할 수 있도록 설계된 자료구조입니다.
# 여기에는 두 가지 중요한 이유가 있습니다:

# 데이터 구조:deque는 이중 연결 리스트(double-linked list)로 구현됩니다.
# 이중 연결 리스트는 각 요소가 이전 및 다음 요소에 대한 참조를 가지고 있어, 양 끝에서의 추가 및 제거 작업이 매우 빠릅니다.
# 반면, 일반 리스트는 동적 배열(dynamic array)로 구현되어 있어, 리스트의 시작 부분에서 요소를 제거하거나 추가할 때 전체 요소를 이동시켜야 하므로 시간이 더 오래 걸립니다.

# 시간 복잡도:deque의 popleft()연산은 O(1) 시간 복잡도를 가집니다. 이는 작업을 수행하는 데 걸리는 시간이 요소의 수와 관계없이 일정하다는 것을 의미합니다.
# 반면, 일반 리스트에서 pop(0)을 사용하면 O(n) 시간 복잡도가 발생합니다. 리스트의 첫 번째 요소를 제거한 후 나머지 모든 요소들을 한 칸씩 앞으로 이동시켜야 하기 때문입니다.
# 따라서 요소의 수가 많을수록 훨씬 더 비효율적입니다.

# //

#수학적으로. 비교하지 않고 가장 빠르게 하는 방법
# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break

# //

#첫시도 시간초과 걸림.
# n = int(input())
# deck = list(range(1, n + 1))
# while len(deck) > 1:
#     deck.pop(0)
#     deck.append(deck.pop(0))
# print(deck[0])

