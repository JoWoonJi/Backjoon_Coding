n = int(input())
words = []

for _ in range(n):
    word = input()
    words.append(word)

words = list(set(words))
words.sort(key=lambda i: (len(i), i)) #len(i)는 짧은길이순, 길이가 같다면 ->두번째i 사전순 sort // 람다함수 정렬함수 다중정렬 가능

for i in words:
    print(i)
