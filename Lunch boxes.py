
t = int(input())

for _ in range(t):
    if _ != 0:
        print()

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    
    a.sort()
    

    total_schools = 0
    for num in a:
        
        if n >= num:
            n -= num
            total_schools += 1
        else:
            break
    print(total_schools)
