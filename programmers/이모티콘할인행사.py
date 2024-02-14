from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    for sale in product([10, 20, 30, 40], repeat=len(emoticons)):
        tmp = [0, 0]
        for rate, money in users:
            m = 0
            for e, s in zip(emoticons, sale):
                if s >= rate:
                    m += e*(100-s)*.01
            if m >= money:
                tmp[0] += 1
            else:
                tmp[1] += m
            if answer[0] < tmp[0] or (answer[0] == tmp[0] and answer[1] < tmp[1]):
                answer = tmp
    return answer
