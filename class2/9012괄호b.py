t=int(input())
for _ in range(t):
    ps=input()
    stack=[]
    vps='YES'
    for c in ps:
        if c=='(':
            stack.append(c)
        elif c==')':
            if not stack or stack[-1]!='(':
                vps='NO'
                break
            stack.pop()
    if stack:
        vps='NO'
    print(vps)