import re

T = int(input())
for i in range(T):
    x = input()
    for it in x:
        c = 0
        if (ord(it) >= 65 and ord(it) <= 90) or (ord(it) >= 97 and ord(it) <= 122) or (ord(it) >= 48 and ord(it) <= 57) or (it == '.') or (it == '-'):
            c = 1
        assert c == 1
    integer_expr = re.compile("(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\\.)+[a-zA-Z]{2,63}$)")
    if integer_expr.match(x):
        print("true")
    else:
        print("false")
