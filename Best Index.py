n=int(input())
a=list(map(int,input().split()))
start=1
k=2
while start<=n:
    start+=k
    k+=1
start-=k-1
k-=2
sums=sum(a[:start])
ma=sums
for i in range(1,n):
    sums-=a[i-1]
    if start<n:
        sums+=a[start]
        start+=1
    else:
        k-=1
        sums-=sum(a[n-k:n])
        start-=k
    if sums>ma:
        ma=sums
print(ma)
