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