import sys

n, m = map(int, input().split())
maxi = 0
x = 0
y = 0
a = [[0]*m for _ in range(n)]
row = [0]*n
col = [0]*m

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        row[i] += a[i][j]
        col[j] += a[i][j]

for i in range(n):
    for j in range(m):
        if row[i] + col[j] - 2 * a[i][j] > maxi:
            x = i
            y = j
            maxi = row[i] + col[j] - 2 * a[i][j]

print(x + 1, y + 1)
