a=input("Enter a string:") 

b="aeiouAEIOU" 

c=0 

for i in a: 
    for j in b: 
      if i==j: 
           c+=1 

print("number of vowels:",c) 