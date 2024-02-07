def solution(info, edges):
    global answer
    answer = 0
    adj = [[] for _ in range(len(info))]
    visited = [0] * len(info)
    for p, c in edges:
        adj[p].append(c)
            
    def dfs(sheep, wolf, nxt):
        global answer
        if wolf >= sheep:
            return
        if sheep > answer:
            answer = sheep
        for i in nxt:
            if not visited[i]:
                visited[i] = 1
                s, w = (sheep, wolf+1) if info[i] else (sheep+1, wolf)
                dfs(s, w, nxt+adj[i])
                visited[i] = 0
                
    dfs(1, 0, adj[0])
                
    return answer
