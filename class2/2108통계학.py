#간결하게
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
m = sorted([int(input()) for _ in range(n)])

def s(m):
    avg = round(sum(m)/n)
    mid = m[n // 2]
    
    freq = Counter(m).most_common()
    max_freq = freq[0][1]
    mods = [i for i, j in freq if j == max_freq]
    mod = mods[1] if len(mods) > 1 else mods[0]
    
    rng = m[-1] - m[0]
    return avg, mid, mod, rng
x = s(m)
for i in x:
    print(i)


# import sys
# from collections import Counter #빈도수 계산해주는 collections모듈의 Counter 클래스

# n = int(sys.stdin.readline().strip())
# nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

# def statistics(nums):
#     nums.sort()
    
#     avg = round(sum(nums) / len(nums))
    
#     median = nums[len(nums) // 2]
    
#     freq = Counter(nums) #{1: 1, 2: 2, 3: 3} 이런식으로 저장 
#     most = freq.most_common() #most_common()메소드, 빈도순으로 내림차순 해줌. [(3, 3), (2, 2), (1, 1)] 이런식으로 저장됨
#     max_freq = most[0][1] # [0]하면 첫번째 튜플 (3,3) 이 저장되고 [0][0] 하면 첫번째 튜플의 첫번째 요소 3, [0][1] 하면 첫번째 튜플의 두번째 요소 3을 가져오게됨
    
#     modes = [i for i, j in most if j == max_freq] #숫자중에 [1]의 값이 max_freq인 것을 찾음
    
#     if len(modes) > 1: # 문제에서 최빈값이 여러개면 두번째 최빈값으로 하라고 했기에 
#         mode = sorted(modes)[1] 
#     else:
#         mode = modes[0]
    
#     range_v = nums[-1] - nums[0]
    
#     return avg, median, mode, range_v

# avg, median, mode, range_v = statistics(nums)

# print(avg)
# print(median)
# print(mode)
# print(range_v)