n = int(input())
scores = list(map(int,input().split()))
m = max(scores)
new_scores= [(i / m) * 100 for i in scores]
new_average = sum(new_scores) / n
print(new_average) 

# new_scores= [(i / m) * 100 for i in scores] 한줄이 

# new_scores = []        

# for i in scores:
#     new_score = (i / m) * 100  
#     new_scores.append(new_score)
# 이렇게 길어진다. 리스트 컴프리헨션 사용법에 익숙해지자
