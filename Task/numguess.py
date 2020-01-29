import random
a=int(input("enter the numbers:"))
print(a)
n=random.randrange(1,5)
if(n==a):
    print("you are winner")
    exit()
else:
    print("you are lose")
    

