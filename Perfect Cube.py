import sys
from collections import defaultdict

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mp = defaultdict(int)
    arr = [0] * 25
    mp[tuple(arr)] += 1
    res = 0
    for i in range(n):
        for j in range(25):
            while a[i] % prime[j] == 0:
                arr[j] += 1
                arr[j] %= 3
                a[i] //= prime[j]
        res += mp[tuple(arr)]
        mp[tuple(arr)] += 1
    print(res)

main()
