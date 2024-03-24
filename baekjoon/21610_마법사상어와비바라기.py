n, m = map(int, input().split())
a = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = {(n, 1), (n, 2), (n - 1, 1), (n - 1, 2)}
answer = 0

for _ in range(m):
    d, s = map(int, input().split())

    tmp = set()
    for x, y in cloud:
        nx = (x+dir[d][0]*s)%n if (x+dir[d][0]*s)%n else n
        ny = (y+dir[d][1]*s)%n if (y+dir[d][1]*s)%n else n
        tmp.add((nx, ny))
    cloud = tmp

    for x, y in cloud:
        a[x][y] += 1

    for x, y in cloud:
        cnt = 0
        for dx, dy in (-1, -1), (-1, 1), (1, -1), (1, 1):
            nx = x+dx
            ny = y+dy
            if 1 <= nx <= n and 1 <= ny <= n and a[nx][ny]:
                cnt += 1
        a[x][y] += cnt

    new = set()
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i][j] >= 2 and (i, j) not in cloud:
                new.add((i, j))
                a[i][j] -= 2
    cloud = new

for x in a:
    answer += sum(x)
print(answer)
