a=input("Enter 1st string:") 

b=input("Enter 2nd string:") 

c=False 

for i in range(0,len(a)-len(b)+1): 

 if (a[i:i+len(b)]==b): 

   c=True 

if c: 

   print(f"'{b}' is present in '{a}'.") 

else: 

 print(f"'{b} is not present in '{a}'.") 