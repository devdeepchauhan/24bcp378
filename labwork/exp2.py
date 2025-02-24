import random

random_list= [random.randint( 1 , 30 ) for _ in range(50)] 
print("generated list:",random_list)

'''user_input=int(input("ENTER ANY NUMBER"))
position=[index for index,value in enumerate(random_list) if value==user_input]

if position:
    print(f"the number{user_input} is found in {position}position ")
else:
    print(f"the number{user_input} is not found in {position}position ") '''

unique_number=list(set(random_list))

print(unique_number)