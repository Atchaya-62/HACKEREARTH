def p(n, p):
    r = 1
    while p:
        if p & 1:
            r = (r * n) % 1000000007
            p -= 1
        p //= 2
        n = (n * n) % 1000000007
    return r

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    x, y = 0, 0
    for i in range(1, n + 1):
        if a[i] % 2:
            x += 1
        else:
            y += 1
    for i in range(1, n):
        j, k = map(int, input().split())
    for _ in range(q):
        j, k = map(int, input().split())
        if a[j] % 2:
            x -= 1
        else:
            y -= 1
        a[j] = k
        if a[j] % 2:
            x += 1
        else:
            y += 1
        print(x * (x + 1) // 2 + y * (y + 1) // 2, end=" ")
    print()
