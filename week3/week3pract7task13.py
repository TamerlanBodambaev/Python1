#part 1 and 2
k = int(input())
for i in range(1, k + 1):
    n = len(str(i))
    s = 0
    for j in str(i):
        s += int(j) ** n
        if i == s:
            print(i, end=' ')


def tg(a1, a2):
    tan = a2 / a1
    return tan

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input())
z2 = int(input())
if tg(x1, x2) < tg(y1, y2) < tg(z1, z2):
    print(f'X({x1, x2})')
    elif tg(y1, y2) < tg(x1, x2) < tg(z1, z2):
        print(f'Y({y1, y2})')
        else:
            print(f'Z({z1, z2}')
