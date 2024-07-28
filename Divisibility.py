
N = int(input())
data = [int(x) for x in input().split()]
j=data[N-1]
if (j % 10==0):
    print("Yes")
else:
    print("No")
