#Recursion
def print_no(n):
    if n==0:
        return
    print("Bye")
    print_no(n-1)
n=int(input("Number of times :"))
print_no(n)