import sys

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = [0] * 26
    for i in range(n):
        a[ord(s[i]) - ord('a')] += 1
    ans = 0
    for i in range(26):
        ans += a[i] // 2
    print(ans)
