from collections import Counter
s=input().upper()
cnt=Counter(s)
max_cnt= max(cnt.values())
max_freq=[]
for ch,ct in cnt.items():
    if ct==max_cnt:
        max_freq.append(ch)
if len(max_freq)>1:
    print('?')
else:
    print(max_freq[0])