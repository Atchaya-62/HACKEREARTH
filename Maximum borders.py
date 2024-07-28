def maxborder(a):
    maxi=0
    for i in range(len(a)):
        count=0
        for j in range(len(a[0])):
            if(a[i][j]=='#'):
                count+=1
                if count> maxi:
                    maxi=count
    return maxi

no=int(input())
while(no!=0):
    t=input().split(" ")
    m=int(t[0])
    n=int(t[1])
    a=[]
    for i in range(m):
        r=[]
        e=str(input())
        if len(e)!=0:
            for x in range(len(e)):
                r.append(e[x])
        a.append(r)
    res=maxborder(a)
    no-=1

    print(res)
