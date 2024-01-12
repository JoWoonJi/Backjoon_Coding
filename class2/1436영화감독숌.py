n = int(input())
def title(n):
    num = 666
    count = 0
    while True:
        if '666' in str(num):
            count += 1
        if count == n:
            return num
        num += 1
print(title(n))

# num은 루프를 통해 계속 1씩 증가하며
# 각 단계마다 '666'을 포함하는지 확인
# num은 666, 667, 668, ... , 1666, 1667, ..로 증가
# 666 다음 666을 포함하는 것은 1666이라는 것이 핵심.
