# AMSTRONG NUMBER

num=int(input())
temp=num
power=len(str(num))  
count=0
while temp>0:
    dig=temp%10         
    count+=dig**power
    temp//=10               
if count==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")