## SQUARE PATTERN

n=int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

## RIGHT ANGLED TRIANGLE
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()