import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

k = int(input())
a = []
for _ in range(k):
    n = int(input())
    if n == 0:
        a.pop()
    else:
        a.append(n)
print(sum(a))
