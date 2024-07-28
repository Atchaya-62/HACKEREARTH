tag = input()                  
li=['A','E','I','O','U','Y']
c1=int(tag[0])+int(tag[1])
c2=int(tag[3])+int(tag[4])
c3=int(tag[4])+int(tag[5])
c4=int(tag[7])+int(tag[8])
if tag[2] in li:
    print("invalid")
elif (c1%2==0 and c2%2==0 and c3%2==0 and c4%2==0 ):
    print("valid")
else:

    print("invalid")
