
# collections 함수 활용해보기 
import collections #collections 함수를 사용하기 위해서는 import 필수

def solution(word):

  # 알파벳별 사용 횟수를 저장할 딕셔너리. collections.Counter함수는 자동으로 사용 횟수를 각각 저장해 준다.apple 이면 내림차순정렬로 Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1}) 
  alphabet_count = collections.Counter(word.lower())

  # 가장 많이 사용된 알파벳 찾기. key로 변환 해야하고. get은 오름차순으로 최대값을 찾아준다. max_char에 문자열로 반환됨. apple이면 p가 들어감.
  max_char = max(alphabet_count, key=alphabet_count.get)

  # 가장 많이 사용된 알파벳이 여러 개인 경우 ? 출력 / values는 딕셔너리 리스트로 바꿀때. (자동 정렬해줌). apple이면 순서에 맞게 a 1 p 2 l 1 e 1 이니까 [1,2,1,1] 이런식으로
  same_cnt = 0
  for same in alphabet_count.values():
    if same == alphabet_count[max_char]: # apple이면 max_char는 p, alphabet_count[p] 는 2다. values [1,2,1,1] 에서 2는 한번 나오니 same_cnt는 1. ?이 출력되지 않는다
        same_cnt += 1
  if same_cnt > 1:
     return "?" 
 
  else:
     return max_char.upper()

word = input()
print(solution(word))


# 처음 버전 
# import collections #collections 함수를 사용하기 위해서는 import 필수

# def solution(word):

#   # 알파벳별 사용 횟수를 저장할 딕셔너리. collections.Counter함수는 자동으로 사용 횟수를 각각 저장해 준다.
#   alphabet_count = collections.Counter(word.lower())

#   # 가장 많이 사용된 알파벳 찾기. key로 변환 해야하고. get은 오름차순으로 최대값을 찾아준다.
#   max_char = max(alphabet_count, key=alphabet_count.get)

#   # 가장 많이 사용된 알파벳이 여러 개인 경우 ? 출력 / values는 자동 정렬해줌. apple이면 순서에 맞게 a 1 p 2 l 1 e 1 이니까 [1,2,1,1] 이런식으로
#   if len([same for same in alphabet_count.values() if same == alphabet_count[max_char]]) > 1:
#     return "?"

#   return max_char.upper()

# word = input()
# print(solution(word))

# 기본 알고리즘 코드
# word = input().lower()      # word = mississipi / baaa
# word_list = list(set(word)) # word_list = ['m', 'i', 's', 'p'] / ['b', 'a'] #set 중복제거
# cnt = []

# for i in word_list:         # i = m, i, s, p / b, a
#     count = word.count(i)     #.count는 횟수를 세는
#     cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]

# if cnt.count(max(cnt)) >= 2:
#     print("?")
# else:
#     print(word_list[(cnt.index(max(cnt)))].upper())