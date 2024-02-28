#다시하기
def count_colored_paper(x, y, n):
    global white, blue 
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                count_colored_paper(x, y, n//2)
                count_colored_paper(x, y+n//2, n//2)
                count_colored_paper(x+n//2, y, n//2)
                count_colored_paper(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white, blue = 0, 0
count_colored_paper(0, 0, N)

print(white)
print(blue)
