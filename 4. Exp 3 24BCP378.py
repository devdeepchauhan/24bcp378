a=input("enter a string:") 

b,c=0,0 

for i in a: 

  if i.isalpha(): 

      b+=1 

  elif i.isdigit(): 

     c+=1 

print("number of alphabets:",b) 

print("number of digits:",c) 