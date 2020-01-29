m=int(input("enter starting number:"))
a=int(input("enter ending number:"))
for val in range(m, a + 1):  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
