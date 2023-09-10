# Examples of sets in python

def create_set():
	my_set = {1, 2, 3, 4, 5}
	print(my_set)

def add_element():
	my_set = {1, 2, 3, 4, 5}
	my_set.add(6)
	print(my_set)

def remove_element():
	my_set = {1, 2, 3, 4, 5}
	my_set.remove(3)
	print(my_set)

def clear_set():
	my_set = {1, 2, 3, 4, 5}
	my_set.clear()
	print(my_set)

def set_union():
	set1 = {1, 2, 3}
	set2 = {4, 5, 6}
	my_set = set1.union(set2)
	print(my_set)

def set_intersection():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.intersection(set2)
	print(my_set)

def set_difference():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.difference(set2)
	print(my_set)

def set_symmetric_difference():
	set1 = {1, 2, 3, 4, 5}
	set2 = {4, 5, 6, 7, 8}
	my_set = set1.symmetric_difference(set2)
	print(my_set)

def set_subset():
	set1 = {1, 2, 3, 4, 5}
	set2 = {2, 3, 4}
	subset = set2.issubset(set1)
	print(subset)

def set_superset():
	set1 = {1, 2, 3, 4, 5}
	set2 = {2, 3, 4}
	superset = set1.issuperset(set2)
	print(superset)

if __name__ == '__main__':
	create_set()   # {1, 2, 3, 4, 5}
	add_element()  # {1, 2, 3, 4, 5, 6}
	remove_element()  # {1, 2, 4, 5}
	clear_set() # set()
	set_union() # {1, 2, 3, 4, 5, 6, 7, 8}
	set_intersection()  # {4, 5}
	set_difference()    # {1, 2, 3} 
	set_symmetric_difference()  # {1, 2, 3, 6, 7, 8}
	set_subset()  # True
	set_superset()   # True 
	

# Typecasting Objects in Python3 into sets

# Typecasting list into set
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 2]
my_set = set(my_list)
print("my_list as a set: ", my_set)
#output: my_list as a set:  {1, 2, 3, 4, 5, 6}

# Typecasting string into set
my_str = "100-Days-of-code"
my_set1 = set(my_str)
print("my_str as a set: ", my_set1)
#output: my_str as a set:  {'-', 'c', 'o', 'f', '1', '0', 'D', 'e', 's', 'h'}

# Typecasting dictionary into set
my_dict = {1: "One", 2: "Two", 3: "Three"}
my_set2 = set(my_dict)
print("my_dict as a set: ", my_set2)
#output: my_dict as a set:  {1, 2, 3}