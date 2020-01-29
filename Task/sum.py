count=1
while(count>0):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    sum=a+b
    print(sum)
    print("do you want to continue (y/n):")
    n=input()
    if n=="y":
        count=1
        continue
    else:
        count=0
        exit()
