def solution(s):
    answer = 1e9
    for k in range(1, len(s)+1):
        l = []
        for i in range(0, len(s), k):
            l.append(s[i:i+k])
        cur = l[0]
        cnt = 1
        res = []
        for i in range(1, len(l)):
            if l[i] == cur:
                cnt += 1
            else:
                if cnt > 1:
                    res.append(str(cnt))
                res.append(cur)
                cur = l[i]
                cnt = 1
        res.append(str(cnt) + cur if cnt > 1 else cur)
        answer = min(answer, len(''.join(res)))
    return answer
