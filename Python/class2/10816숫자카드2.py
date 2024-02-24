from collections import Counter #요소별 개수 세어주는 함수
#import sys 해봤으나 속도 같음 

n = int(input()) 
n_cards = list(map(int, input().split()))  
m = int(input()) 
m_cards = list(map(int, input().split())) 

counting = Counter(n_cards)

result = [counting[i] for i in m_cards]
print(' '.join(map(str, result)))

# //

# n = int(input()) 
# cards = list(map(int, input().split()))  
# m = int(input()) 
# numbers = list(map(int, input().split())) 
# 딕셔너리, 속도 차이 없음 
# cards_count = {}
# for i in cards:
#     if i in cards_count:
#         cards_count[i] += 1
#     else:
#         cards_count[i] = 1

# result = [cards_count.get(number, 0) for number in numbers]
# print(' '.join(map(str, result)))

# //

#이진탐색 1920수찾기에서 사용했던. 더 빠를줄 알았지만 두배는 더 느림
# from bisect import bisect_left, bisect_right

# n = int(input()) 
# cards = list(map(int, input().split()))  
# m = int(input()) 
# numbers = list(map(int, input().split())) 

# cards.sort()

# def count_by_range(arr, left_value, right_value):
#     right_index = bisect_right(arr, right_value)
#     left_index = bisect_left(arr, left_value)
#     return right_index - left_index

# result = [count_by_range(cards, number, number) for number in numbers]

# print(' '.join(map(str, result)))