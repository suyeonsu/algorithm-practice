from itertools import combinations

n = int(input())
exp = list(input())

nums = []
op = []
i = 0
while i < len(exp):
    if '0' <= exp[i] <= '9':
        nums.append(int(exp[i]))
        if len(nums) == 2 and op:
            b, a = nums.pop(), nums.pop()
            nums.append(eval(str(a) + op.pop() + str(b)))
    else:
        op.append(exp[i])
    i += 1
answer = nums.pop()

for k in range(1, n//2):
    for comb in combinations(range(1, n, 2), k):
        for i in range(len(comb)-1):
            if comb[i]+2 == comb[i+1]:
                break
        else:
            _tmp = exp[:]
            for i in comb:
                _tmp[i-1] = '(' + _tmp[i-1]
                _tmp[i+1] = _tmp[i+1] + ')'
            tmp = []
            for x in _tmp:
                tmp += list(x)
            nums = []
            op = []
            i = 0
            while i < len(tmp):
                if '0' <= tmp[i] <= '9':
                    nums.append(int(tmp[i]))
                    while len(nums) >= 2 and op:
                        b, a = nums.pop(), nums.pop()
                        nums.append(eval(str(a) + op.pop() + str(b)))
                else:
                    if tmp[i] == '(':
                        nums.append(eval(''.join(tmp[i+1:i+4])))
                        while len(nums) >= 2 and op:
                            b, a = nums.pop(), nums.pop()
                            nums.append(eval(str(a) + op.pop() + str(b)))
                        i += 4
                    else:
                        op.append(tmp[i])
                i += 1
            answer = max(answer, nums.pop())
print(answer)
