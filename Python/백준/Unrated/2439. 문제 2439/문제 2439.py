a = int(input())
for i in range(a) :
    print(" " * (a - 1 - i), end = "")
    print("*" * (i + 1))