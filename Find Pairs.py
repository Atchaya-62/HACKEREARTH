def check(a, x):
    n = len(a)
    r = 0
    odd = 0
    for v in a:
        odd += v & 1
    i = 0
    j = n - 1
    while i < j:
        odd -= a[i] & 1
        while i < j and a[i] + a[j] > x:
            odd -= a[j] & 1
            j -= 1
        r += (j - i - odd) if a[i] & 1 else odd
        i += 1
    return r

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(check(a, y) - check(a, x - 1))
