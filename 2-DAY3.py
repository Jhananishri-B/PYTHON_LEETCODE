n=input()
rev=""
l=len(n)-1
for i in range(l,-1,-1):
    rev+=n[i]
print(rev)
