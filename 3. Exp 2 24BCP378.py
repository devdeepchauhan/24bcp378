a=input("Enter a string:") 

b="" 

for i in a: 
 if "A"<=i<="Z": 

   b=b+chr(ord(i)+32) 

 elif "a"<=i<="z": 

   b=b+chr(ord(i)-32) 
 else: 
   b+=i 

print(b) 