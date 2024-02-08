def solution(enroll, referral, seller, amount):
    answer = []
    info = {e: [r, 0] for e, r in zip(enroll, referral)}
    
    def dfs(child, money):
        p = info[child][0]
        fee = int(money*0.1)
        info[child][1] += money-fee
        if p != "-" and fee > 0:
            dfs(p, fee)
        
    for s, a in zip(seller, amount):
        dfs(s, a*100)
    
    for e in enroll:
        answer.append(info[e][1])
    
    return answer
