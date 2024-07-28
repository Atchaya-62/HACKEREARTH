n=int(input())
c,f,k=map(int,input().split())
s,b,m,g=map(int,input().split())


on=c+(n-f)*k
cl=b+(n/s)*m+n*g

if(on<cl):
    print("Online Taxi")

else:
    print("Classic Taxi")
