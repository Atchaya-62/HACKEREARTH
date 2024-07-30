import sys

for line in sys.stdin:
    t = int(line)
    for _ in range(t):
        n, m, k = map(int, input().split())
        print((n + k - 1) // k + (m + k - 1) // k)
