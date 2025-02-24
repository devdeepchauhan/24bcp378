def fac(x): 

   fa=1 

   if(x==0): 

    return 1 

   for i in range(1,x+1): 

     fa=fa*i 

   return fa 

a=int(input("enter value of n:")) 

b=int(input("enter value of r:")) 

nCr=float(fac(a)/(fac(a-b)*fac(b))) 

nPr=float(fac(a)/fac(a-b)) 

print("nCr =",nCr) 

print("nPr =",nPr) 