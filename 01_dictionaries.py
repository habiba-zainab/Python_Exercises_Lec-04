"""

===========================================================
   LECTURE 04 - SET 01 : BASICS OF DICTIONARY
   Topics : Dictionary Basics - Creating, Accessing, Modifying
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Dictionary Creation
# ==========================================================

# Q1: Create different types of dictionaries
#    Create:
#    - Empty dictionary
#    - Dictionary with string keys (person info: name,
#              age, city)
#    - Dictionary with integer keys (roll number: name)
#    - Dictionary with mixed value types
#    - Dictionary using dict() constructor
#    Print each dictionary

print("\n--- Q1: Creating Dictionaries ---")

empty = {}
person = {'name' : 'John', 'age': 25, 'city' : 'NYC'}
students = {101: 'alice', 102: 'Bob', 103: 'Charlie'}
mixed = {'name' : 'Product', 'price' : 99.99, 'available' : True, 'stock' : 50}
using_dict = dict(a=1, b=2, c=3)

print("Empty:", empty)
print("Person: ", person)
print("Students: ", students)
print("Mixed: ", mixed)
print("Using dict: ", using_dict)

# ----------------------------------------------------------

# Q2: Dictionary from two lists
#    Given:   keys = ['name', 'age', 'city', 'country']
#             values = ['Alice', 23, 'Paris', 'France']
#    Create dictionary by combining these lists
#    Use zip() and dict()
