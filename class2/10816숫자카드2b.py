from collections import Counter
n=int(input())
n_cards=list(map(int,input().split()))
m=int(input())
m_cards=list(map(int,input().split()))
counting=Counter(n_cards)
result=[counting[i] for i in m_cards]
print(' '.join(map(str,result)))
