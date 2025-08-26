#pass by reference
def sum(x):
    x+=4
    print(x)
n=int(input())
sum(n)
print(n)
