from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    want = {w: n for w, n in zip(want, number)}
    for i in range(len(discount)-9):
        for item, cnt in want.items():
            if discount[i:i+10].count(item) != cnt:
                break
        else:
            answer += 1
    return answer
