a = int(input("Enter maths marks :"))
b = int(input("Enter physics marks :"))
c = int(input("Enter chemistry marks :"))

if a<=39 or b <=39 or c <= 39:
    print("Fail")

else:
    total= a+b+c
    average=total/3
    print(f"The total of the marks is : {total}")
    print(f"The average of the marks is : {average}")

    def grade(marks):
        if marks <=39:
            return "F"
        elif 45 <= marks <= 49:
           return "P"
        elif 45 <= marks <= 49:
            return "C"
        elif 50 <= marks <= 54:
            return"B"
        elif 55 <= marks <= 59:
            return"B+"
        elif 60 <= marks <= 69:
            return"A"
        elif 70 <= marks <= 79:
            return"A+"
        elif 80 <= marks <= 100:
            return"O"
print(f"Maths Grade : {grade(a)}")
print(f"physics Grade : {grade(b)}")
print(f"chemistry Grade : {grade(c)}")
