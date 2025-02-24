import random

random_list= [random.randint( -10, 10 ) for _ in range(10)] 
print("generated list:",random_list)

positive_number=[ num for num in random_list if num > 0]
negative_number=[ num for num in random_list if num < 0]

print(positive_number)
print(negative_number)