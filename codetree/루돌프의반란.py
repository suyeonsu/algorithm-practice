n, m, p, c, d = map(int, input().split())
rx, ry = map(int, input().split())
santa = [[0, 0]] * (p+1)
for _ in range(p):
    i, x, y = map(int, input().split())
    santa[i] = [x, y]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dead = set()
stun = [[] for _ in range(m+2)]
calc = lambda x1, y1, x2, y2: (x1-x2)**2 + (y1-y2)**2
score = [0] * (p+1)

def kick_santa(idx, dx, dy):
    for i, (sx, sy) in enumerate(santa):
        if i != 0 and i != idx and santa[idx][0] == sx and santa[idx][1] == sy:
            nx = sx+dx
            ny = sy+dy
            if 1 <= nx <= n and 1 <= ny <= n:
                santa[i] = [nx, ny]
                kick_santa(i, dx, dy)
            else:
                dead.add(i)
                santa[i] = [0, 0]

for k in range(1, m+1):

    min_dist = 1e9
    min_santa = 0
    for idx, (sx, sy) in enumerate(santa):
        if idx != 0 and idx not in dead:
            dist = calc(sx, sy, rx, ry)
            if dist < min_dist:
                min_dist = dist
                min_santa = idx
            elif dist == min_dist:
                if santa[min_santa][0] < sx or (santa[min_santa][0] == sx and santa[min_santa][1] < sy):
                    min_santa = idx
    dx, dy = 0, 0
    sx, sy = santa[min_santa]
    if sx-rx > 0:
        dx = 1
    elif sx-rx < 0:
        dx = -1
    if sy-ry > 0:
        dy = 1
    elif sy-ry < 0:
        dy = -1
    rx += dx
    ry += dy

    for idx, (sx, sy) in enumerate(santa):
        if idx != 0 and idx not in dead and rx == sx and ry == sy:
            score[idx] += c
            nx = sx+dx*c
            ny = sy+dy*c
            if 1 <= nx <= n and 1 <= ny <= n:
                santa[idx] = [nx, ny]
                stun[k].append(idx)
                stun[k+1].append(idx)
                kick_santa(idx, dx, dy)
            else:
                dead.add(idx)
                santa[idx] = [0, 0]
            if len(dead) == p:
                k = m+1
                break
    
    if k == m+1:
        break
    
    for idx, (sx, sy) in enumerate(santa):
        if idx != 0 and idx not in stun[k] and idx not in dead:
            min_dist = 1e9
            nxt_d = -1
            for rank, (dx, dy) in enumerate(direction):
                nx = sx+dx
                ny = sy+dy
                if 1 <= nx <= n and 1 <= ny <= n and [nx, ny] not in santa and calc(nx, ny, rx, ry) < calc(sx, sy, rx, ry):
                    dist = calc(nx, ny, rx, ry)
                    if dist < min_dist:
                        min_dist = dist
                        nxt_d = rank
                    elif dist == min_dist and rank < nxt_d:
                        nxt_d = rank
            if nxt_d != -1:
                santa[idx][0] += direction[nxt_d][0]
                santa[idx][1] += direction[nxt_d][1]

                if santa[idx][0] == rx and santa[idx][1] == ry:
                    score[idx] += d
                    reverse = nxt_d+2 if nxt_d <= 1 else nxt_d-2
                    nx = santa[idx][0] + direction[reverse][0]*d
                    ny = santa[idx][1] + direction[reverse][1]*d
                    if 1 <= nx <= n and 1 <= ny <= n:
                        santa[idx] = [nx, ny]
                        stun[k].append(idx)
                        stun[k+1].append(idx)
                        kick_santa(idx, direction[reverse][0], direction[reverse][1])
                    else:
                        dead.add(idx)
                        santa[idx] = [0, 0]
                    if len(dead) == p:
                        k = m+1
                        break

    if k == m+1:
        break
    
    for i in range(1, p+1):
        if i not in dead:
            score[i] += 1

print(' '.join([str(s) for s in score if s]))
