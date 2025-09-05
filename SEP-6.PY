#print n to 1 using recursion
def print_num(n):
    if n==0:
        return
    print(n)
    print_num(n-1)
n=int(input("Enter number:"))
print_num(n)