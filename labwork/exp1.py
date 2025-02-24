# A list contains names of boys and girls as its elements. Boys names are stored as tuples.write a program to find out number of boys and girls in the list

names = [("John",), "Emma", ("Mike",), "Sophia", ("David",), "Olivia", "Lily"]
def count_boys_girls(names_list):
    boys_count = sum(1 for name in names_list if isinstance(name, tuple))
    girls_count = sum(1 for name in names_list if isinstance(name, str))
    
    return boys_count, girls_count


boys, girls = count_boys_girls(names)

print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
