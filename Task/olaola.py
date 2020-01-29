def ola():
    while True:
        src=int(input("enter your source:"))
        des=int(input("enter your destination:"))
        km=des-src
        print("1.mini\n 2.micro\n 3.prime")
        print("enter ur choice:")
        n=int(input())
        if(n==1):
            mini(km)
        elif(n==2):
            micro(km)
        elif(n==3):
            prime(km)
        else:
            print("invalid")
        continue
    return true

def mimi(km):
        print("total kilometer:",km)
        price=km*5
        print("price",price)
        ola ()
        return true

def micro(km):
        print("total kilometer:",km)
        price=km*7
        print("price",price)
        ola()
        return true
        
       
def prime(km):
        print("total kilometer:",km)
        price=km*10
        print("price",price)
        ola()
        return true
print("welcome")
ola()
