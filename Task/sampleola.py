count=1
while(count>0):
    src=int(input("enter your source:"))
    des=int(input("enter your destination:"))
    km=des-src
    print("1.mini\n 2.macro\n 3.prime")
    print("enter ur choice:")
    n=int(input())
    if(n==1):
        print("total kilometer:",km)
        price=km*5
        print("price",price)
        count=1
        continue
    elif(n==2):
        print("total kilometer:",km)
        price=km*7
        print("price",price)
        count=1
        continue
    elif(n==3):
        print("total kilometer:",km)
        price=km*10
        print("price",price)
        count=1
        continue
    else:
        print("invalid")
        continue
    count=1
else:
    exit()
    
