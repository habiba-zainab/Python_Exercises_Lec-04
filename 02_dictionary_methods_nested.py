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
