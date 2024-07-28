t=int(input())
mini=[]
while(t>0):
    a,b=[int(x) for x in input().split()]
    n=int(input())
    c1,c2=0,0
    while n>0:
        i,j=[int(x) for x in input().split()]
        c1+=a*i+b*j
        c2+=a*j+b*i
        n-=1
    mini.append(min(c1,c2))
    t-=1
for i in mini:
    print(i)
