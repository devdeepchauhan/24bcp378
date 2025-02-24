import math

a = int(input("Enter x cordinate of centre : "))
b = int(input("Enter y cordinate of centre : "))
c = int(input("Enter radius of circle : "))
d = int(input("Enter x coordinate of the point : "))
e = int(input("Enter y coordinate of the point : "))
distance = math.sqrt(pow(d-a,2) + pow(e-b,2))

if(distance<c):
     print("Point lies inside the circle.")
elif(distance == c):
    print("Point lies on the circle.")
else:
    print("Point lies outside the circle.")
