while True:
    s = input()
    if s == '.':
        break

    stack = []
    balanced = 'yes'
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')': #짝이 맞는지 확인해야하기 때문에 [랑 별도로
            if not stack or stack[-1] != '(': #스택에 [가 와버리면 pop이 꼬이기 때문에 -1마지막이 (인지 아닌지
                balanced = 'no'
                break
            stack.pop() # )있으면 (가 마지막이기 때문에 짝인 (를 제거. yes라면 ([])나 [()] 밖에 없다.
        elif c == ']':
            if not stack or stack[-1] != '[':
                balanced = 'no'
                break
            stack.pop()

    if stack: # 스택이 비어있지않다면 
        balanced = 'no'

    print(balanced) #처음 yes였기때문에 다 돌고 no가 아니라면 yes하고 그다음줄.