# Sample script to explore built-in data structures

# --- Lists ---
print("=== Lists ===")
# Lists are mutable, ordered collections.
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Appending to a list
my_list.append(6)
print("After appending 6:", my_list)

# Removing from a list
my_list.remove(3)
print("After removing 3:", my_list)

# Accessing elements by index
print("Element at index 2:", my_list[2])

# Slicing a list
print("Slice of the list (index 1 to 3):", my_list[1:4])

# Checking if an element exists
print("Is 4 in the list?", 4 in my_list)

# --- Tuples ---
print("\n=== Tuples ===")
# Tuples are immutable, ordered collections.
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Accessing elements by index (same as lists)
print("Element at index 1 in tuple:", my_tuple[1])

# Slicing a tuple
print("Slice of the tuple (index 2 to 4):", my_tuple[2:5])

# Checking if an element exists
print("Is 3 in the tuple?", 3 in my_tuple)

# --- Sets ---
print("\n=== Sets ===")
# Sets are unordered, mutable collections that do not allow duplicates.
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding elements to a set
my_set.add(6)
print("After adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)  # Will raise KeyError if element doesn't exist
print("After removing 3:", my_set)

# Checking if an element exists
print("Is 5 in the set?", 5 in my_set)

# Set operations (Union, Intersection, Difference)
other_set = {4, 5, 6, 7, 8}
print("Union of sets:", my_set | other_set)
print("Intersection of sets:", my_set & other_set)
print("Difference of sets:", my_set - other_set)

# --- Dictionaries ---
print("\n=== Dictionaries ===")
# Dictionaries are unordered collections of key-value pairs.
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}
print("Original dictionary:", my_dict)

# Adding or updating key-value pairs
my_dict["age"] = 26  # Updating existing key
my_dict["country"] = "Fictional Land"  # Adding new key-value pair
print("After updating 'age' and adding 'country':", my_dict)

# Accessing values by key
print("Value of 'name':", my_dict["name"])

# Checking if a key exists
print("Is 'city' a key in the dictionary?", "city" in my_dict)

# Iterating over keys and values
print("Iterating over dictionary items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Removing key-value pairs
del my_dict["city"]
print("After deleting 'city' key:", my_dict)

# --- Performance Comparisons ---
print("\n=== Performance Comparisons ===")

# List: Time complexity for accessing an element by index
import time
start_time = time.time()
_ = my_list[3]  # Accessing element by index
print("List access time:", time.time() - start_time)

# Tuple: Time complexity for accessing an element by index
start_time = time.time()
_ = my_tuple[3]
print("Tuple access time:", time.time() - start_time)

# Set: Time complexity for checking existence (O(1) average time)
start_time = time.time()
print("Is 4 in set?", 4 in my_set)
print("Set membership test time:", time.time() - start_time)

# Dictionary: Time complexity for checking existence of a key (O(1) average time)
start_time = time.time()
print("Is 'age' a key in dictionary?", "age" in my_dict)
print("Dictionary key membership test time:", time.time() - start_time)
