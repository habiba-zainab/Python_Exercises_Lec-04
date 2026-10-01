"""

==================================================================
   LECTURE 04 - SET 02 : DICTIONARY METHODS & NESTED DICTIONARIES
   Topics : Dictionary Methods and Nested Dictionaries
   Total Questions :  
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
