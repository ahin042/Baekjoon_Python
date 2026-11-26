import sys

c = int(sys.stdin.readline())
n = []
for i in range(c):
    a, b = map(int, sys.stdin.readline().split())
    n.append(a + b)
print('\n'.join(map(str, n)))