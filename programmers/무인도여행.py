from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                dq = deque([(i, j)])
                visited[i][j] = 1
                s = eval(maps[i][j])
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                            dq.append((nx, ny))
                            visited[nx][ny] = 1
                            s += eval(maps[nx][ny])
                answer.append(s)
    return sorted(answer) if answer else [-1]
