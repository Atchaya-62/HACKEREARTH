import sys

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    t = input()
    cnt = [0] * 26
    for ch in t:
        cnt[ord(ch) - ord('a')] += 1
    wildcard = 0
    for ch in s:
        if ch == '?':
            wildcard += 1
        else:
            cnt[ord(ch) - ord('a')] -= 1
    for i in range(26):
        wildcard -= max(0, cnt[i])
    print("Yes" if wildcard >= 0 else "No")
