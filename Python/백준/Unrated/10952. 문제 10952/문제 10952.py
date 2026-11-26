a = 1 ; b = 1
n = []
while (a != 0 and b != 0) :
    a,b = map(int,input().split())
    if a == 0 and b == 0 :
        break
    n.append(a + b)
for i in n :
    print(i)