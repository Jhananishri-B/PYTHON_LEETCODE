def print_name(name, n):
    if n==0:
        return
    print(name)  
    print_name(name,n-1)
user_name=input("Enter your name: ")
times=int(input("Number of times : "))
print_name(user_name,times)
