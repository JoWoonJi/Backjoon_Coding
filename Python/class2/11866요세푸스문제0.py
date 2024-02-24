n, k = map(int, input().split())

josephus = []
people = list(range(1, n+1))
index = 0

while people:
    index = (index + k - 1) % len(people) #k-1 인덱스가 0부터 시작하므로 people의 숫자가 하나씩 줄어드는것이 요세푸스의 핵심
    josephus.append(people.pop(index)) #한명씩 빼주는 pop. 스택에서 쓰는 것처럼 파이썬에도 구현되어있다.

print("<" + ", ".join(map(str, josephus)) + ">") # 그대로 출력하면 [ ] 리스트 형태인데  < >집합?을 요구하므로

# 첫 번째 반복:

# 초기 people: [1, 2, 3, 4, 5, 6, 7]
# index = (0 + 3 - 1) % 7 = 2
# 제거된 사람: people[2] 즉, 3
# 업데이트된 people: [1, 2, 4, 5, 6, 7]

# 두 번째 반복:

# 현재 people: [1, 2, 4, 5, 6, 7]
# index = (2 + 3 - 1) % 6 = 4
# 제거된 사람: people[4] 즉, 6
# 업데이트된 people: [1, 2, 4, 5, 7]