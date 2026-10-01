"""

==================================================================
   LECTURE 04 - SET 02 : DICTIONARY METHODS & NESTED DICTIONARIES
   Topics : Dictionary Methods and Nested Dictionaries
   Total Questions :  06
==================================================================

"""
# ==========================================================
# PART A:   Basic Dictionary Methods
# ==========================================================

# Q1:  keys(), values(), items() methods
#    Given: book = {'title': 'Atomic Habits', 
#      'author': 'James Clear', 'year': 2018, 'pages': 320}
#    Use:
#    - keys() to get all keys
#    - values() to get all values
#    - items() to get key-value pairs
#    Convert to lists and print

print("\n--- Q1: keys(), values(), items() ---")

book = {'title': 'Atomic Habits', 'author': 'James Clear', 'year': 2018, 'pages': 320}
print("Book: ", book)

keys = list(book.keys())
values = list(book.values())
items = list(book.items())

print("Keys: ", keys)
print("Values: ", values)
print("Items: ", items)

# ----------------------------------------------------------

# Q2:  get() method with default values
#    Given: settings = {'theme': 'dark', 'language': 'en',
#                          'notifications': True}
#    Get:
#    - 'theme' (exists)
#    - 'font_size' (doesn't exist, no default)
#    - 'font_size' (doesn't exist, default 12)
#    - 'volume' (doesn't exist, default 50)

print("\n--- Q2: get() method ---")

settings = {'theme': 'dark', 'language': 'en', 'notifications': True}
print("Settings: ", settings)

print("theme:", settings.get('theme'))
print("font_size (no default):", settings.get('font_size'))
print("font_size (default 12):", settings.get('font_size', 12))
print("volume (default 50):", settings.get('volume', 50))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Dictionary Modification Methods
# ==========================================================

# Q3:  update() method
#    Given:     profile = {'name' : 'Stacey', 'age' : 23}
#    Update with: 
#    - {'age' : 24, 'city' : 'London'}
#    - {'job' : Engineer, 'city' : 'Edinburgh'}
#    Show that existing keys are overwritten

print("\n--- Q3: update() method ---")

profile = {'name' : 'Stacey', 'age' : 23}
print("Original: ", profile)

profile.update({'age' : 24, 'city' : 'London'})
print("After first update: ", profile)

profile.update({'job' : 'Engineer', 'city' : 'Edinburgh'})
print("After second update: ", profile)

# ----------------------------------------------------------

# Q4:  pop() and popitem() methods
#    Given: data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#    - Pop 'b' and store the value
#    - Pop 'z' with default value 0
#    - Pop last item using popitem()
#    Print removed values and remaining dictionary

print("\n--- Q4: pop() & popitem() ---")

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original: ", data)

popped_b = data.pop('b')
print("Popped 'b': ", popped_b)
print("After pop: ", data)

popped_z = data.pop('z', 0)
print("Popped 'z' (with default): ", popped_z)

last_item = data.popitem()
print("Popped last item: ", last_item)
print("Final: ", data)

# ----------------------------------------------------------

# ==========================================================
# PART C:   Dictionary Utility Methods
# ==========================================================

# Q5:  clear() and copy() methods
#    Given:  original = {'x' : 10, 'y' : 20, 'z' : 30}
#    - Create shallow copy
#    - Modify copy
#    - Show original is unchanged
#    - Clear the copy
#    - Show original still has data

print("\n--- Q5: clear() & copy() ---")

original = {'x' : 10, 'y' : 20, 'z' : 30}
print("Original: ", original)

copy_dict = original.copy()
print("Copy: ", copy_dict)

copy_dict['y'] = 999
print("Modified copy:", copy_dict)
print("Original unchanged:", original)

copy_dict.clear()
print("After clear():", copy_dict)
print("Original still intact:", original)

# ----------------------------------------------------------

# Q6:  fromkeys() method
#    Create dictionaries using fromkeys():
#    - From list ['a', 'b', 'c'] with default value 0
#    - From tuple ('x', 'y', 'z') with default value []
#    - From range(1, 6) with default value 'number'

print("\n--- Q6: fromkeys() method ---")

from_list = dict.fromkeys(['a', 'b', 'c'], 0)
print("From list: ", from_list)

from_tuple = dict.fromkeys(('x', 'y', 'z'), [])
print("From tuple: ", from_tuple)

from_range = dict.fromkeys(range(1,6), 'number')
print("From range: ", from_range)

# ----------------------------------------------------------

# ==========================================================
# PART D:   Nested Dictionary Method
# ==========================================================

# Q7:  Modify nested dictionary
#    Given nested structure, perform operations:
#    - Add new key to inner dictionary
#    - Update value in nested dict
#    - Delete key from nested dict
#    - Add entire new nested section

print("\n--- Q7: Modify Nested Dictionary ---")

org = {'dept1': {'manager' : 'Alice', 'budget' : 100000}}
print("Original: ")
print(org)
print()

org['dept1']['employees'] = 10
print("After adding 'employees': ")
print(org)
print()

org['dept1']['budget'] = 120000
print("After updating budget: ")
print()

org['dept2'] = {'manager': 'Bob', 'budget': 80000}
print("After adding dept2:")
print(org)