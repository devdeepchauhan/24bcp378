def fac(x): 

   fa=1 

   for i in range(1,x+1): 

    fa=fa*i 

   return fa 

a=float(input("enter value of degree:")) 

b=a*(3.14159/180) 

sum=0 

for i in range(1,5): 

 c=float(((-1)**(i+1))*(b**((2*i)-1))/fac((2*i)-1)) 

sum=sum+c 

print("Sin","(",a,")","=",sum) 