c = int(input())
n = []
for i in range(c) :
    a,b = map(int,input().split())
    n.append(a + b)
for i in n :
    print(i)