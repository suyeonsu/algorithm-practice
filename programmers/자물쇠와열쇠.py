def solution(key, lock):
    answer = False
    n, m = len(lock), len(key)
    k = n+(m-1)*2
    nlock = [[0]*k for _ in range(k)]
    for i in range(n):
        for j in range(n):
            nlock[i+m-1][j+m-1] = lock[i][j]
    for _ in range(4):
        key = list(map(list, zip(*key[::-1])))
        for i in range(k-m+1):
            for j in range(k-m+1):
                tmp = [l[:] for l in nlock]
                for x in range(m):
                    for y in range(m):
                        if tmp[i+x][j+y] == 1 and key[x][y] == 1:
                            y = m
                            x = m
                            break
                        if tmp[i+x][j+y] == 0 and key[x][y] == 1:
                            tmp[i+x][j+y] = 1
                if all(tmp[x][y] == 1 for x in range(m-1, k-(m-1)) for y in range(m-1, k-(m-1))):
                    answer = True
    return answer
