tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2  # Joining two tuples
print("Joined Tuple:", joined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

result_tuple = tuple1 * 2 # Repeating the first tuple
print("Repeated Tuple:", result_tuple)  # Output: (1, 2, 3, 1, 2, 3)

name = ('alice', 'bob', 'charlie')
ages = (25, 30, 35)
result_tuple1 = tuple(zip(name, ages))  # Zipping two sequences into a tuple
print("Zipped Tuple:", result_tuple1)  # Output: (('alice', 25), ('bob', 30), ('charlie', 35))
 