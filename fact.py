num=int(input("enter a number"))
fact=1
if num<0:
    print("pleasr enter a positive number")
elif num==0:
    print("the factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of",num,"is",fact)
