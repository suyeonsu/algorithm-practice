from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]    
    adj = defaultdict(list)
    out = defaultdict(int)
    for a, b in edges:
        adj[a].append(b)
        out[a] += 1
        if b in out:
            del out[b]
    for node, cnt in out.items():
        if cnt >= 2:
            answer[0] = node
            break
    
    for srt in adj[answer[0]]:
        visited = set()
        dq = deque(adj[srt])
        v, e = 1, 0
        visited.add(srt)
        while dq:
            cur = dq.popleft()
            for nxt in adj[cur]:
                if (cur, nxt) not in visited:
                    e += 1
                    visited.add((cur, nxt))
                    if nxt not in visited:
                        v += 1
                        visited.add(nxt)
                    dq.append(nxt)
        if v+1 == e:
            answer[3] += 1
        elif v-1 == e:
            answer[2] += 1
        elif v == e:
            answer[1] += 1
    return answer
