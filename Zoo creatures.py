def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = lcm(a, b)
    print(x // a, x // b)
