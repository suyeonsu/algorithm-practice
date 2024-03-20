"""
0, 0에서 크기 1, 오른쪽 방향으로 시작
매 초 이동함
머리 부분을 다음 칸에 위치하였을 때,
- 이동 위치 == 벽 or 자신의 몸 -> 게임 종료
- 이동 위치 == 사과 -> 사과 삭제, 크기 += 1
- 이동 위치 != 사과 -> 계속 이동

양방향 큐 deque를 이용
dq[0] == 꼬리, dq[-1] == 머리
snake = deque([0, 0]) 부터 게임 시작

시간 = 0
게임 종료 전까지,
    머리 = snake[-1]
    머리의 x, y에 방향에 따라 dx, dy를 더하여 nx, ny 구함 ( == 머리 이동)
    0. nx, ny가 범위 밖이거나 snake에 해당 좌표가 존재
        게임 종료
    1. 사과 o
        사과 없앰, snake의 맨 뒤에 (nx, ny) 추가
    2. 사과 x
        snake 맨 앞을 삭제, (nx, ny) 추가
    시간 += 1
    다음 방향 = 방향[시간]
"""

from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
dir = [0] * 10000
l = int(input())
for _ in range(l):
    x, c = input().split()
    dir[int(x)] = c

s = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur = 0
snake = deque([(0, 0)])
while True:
    s += 1
    x, y = snake[-1]
    nx, ny = x+d[cur][0], y+d[cur][1]
    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake:
        snake.append((nx, ny))
        if board[nx][ny]:
            board[nx][ny] = 0
        else:
            snake.popleft();
        if dir[s] == 'L':
            cur -= 1
            if cur == -1:
                cur = 3
        elif dir[s] == 'D':
            cur += 1
            if cur == 4:
                cur = 0
    else:
        break
print(s)
