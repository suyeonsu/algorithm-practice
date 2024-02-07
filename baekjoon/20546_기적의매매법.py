m = int(input())
stock = list(map(int, input().split()))

a = [m, 0]
for x in stock:
    if x <= a[0]:
        a[1] += a[0]//x
        a[0] -= x*(a[0]//x)
b = [m, 0]
for x, y, z, s in zip(stock, stock[1:], stock[2:], stock[3:]):
    if x < y < z and b[1]:
        b[0] += s*b[1]
        b[1] = 0
    elif x > y > z and s <= b[0]:
        b[1] += b[0]//s
        b[0] -= s*(b[0]//s)

if a[0]+stock[-1]*a[1] == b[0]+stock[-1]*b[1]:
    print("SAMESAME")
elif a[0]+stock[-1]*a[1] > b[0]+stock[-1]*b[1]:
    print("BNP")
else:
    print("TIMING")
