## INVERTED TRIANGLE

n=int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

## HOLLOW TRIANGLE

n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==i or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
