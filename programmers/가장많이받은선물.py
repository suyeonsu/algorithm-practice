def solution(friends, gifts):
    answer = 0
    gift = {f: {f: 0 for f in friends} for f in friends}
    point = {f: 0 for f in friends}
    for g in gifts:
        a, b = g.split()
        gift[a][b] += 1
        point[a] += 1
        point[b] -= 1
    for a in friends:
        cnt = 0
        for b in friends:
            if a != b:
                if gift[a][b] > gift[b][a] or (gift[a][b] == gift[b][a] and point[a] > point[b]):
                    cnt += 1
        answer = max(answer, cnt)
    return answer
