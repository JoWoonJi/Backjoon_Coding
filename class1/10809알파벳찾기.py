# s = input()
# a = 'abcdefghijklmnopqrstuvwxyz'
# l = [-1]*26

# for i in range(len(s)):
#     if l[a.index(s[i])] == -1: #index 함수. 첫번째 인덱스 찾는. // -1로 초기화 되어있기 때문에 apple 같은 경우에 두번째 p를 계산하지 않게 해줌
#         l[a.index(s[i])] = i
    
# for i in range(len(l)):
#     print(l[i], end=" ")

# 더 간단하게. find 함수 사용. 처음 나타나는 인덱스 반환. 못찾으면 기본 -1 반환한다. 이걸 학습하라는 문제인듯.
s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha: #알파벳 a 가 s에서 몇번째 인지
    print(s.find(i), end = " ")