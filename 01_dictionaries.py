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

print("\n--- Q2: Create from Lists ---")

keys = ['name', 'age', 'city', 'country']
values = ['Alice', 23, 'Paris', 'France']

print("Keys: ", keys)
print("Values: ", values)
print()

combined = dict(zip(keys, values))
print("Dictionary: ", combined)

# ----------------------------------------------------------

# ==========================================================
# PART B:   Accessing Dictionary Values
# ==========================================================

# Q3: Access dictionary values
#    Given: 
#         student = {'name' : 'Alice', 'age' : 20, 
#                    'grade' : 'A', 'gpa' : 3.8}
#    Access: 
#    - Name using student ['name']
#    - Age using student  ['age']
#    - Use get() method to safely access 'course'

print("\n--- Q3: Accessing Values ---")

student = {'name' : 'Alice', 'age' : 20, 'grade' : 'A', 'gpa' : 3.8}
print("Student:", student)

print("Name:", student['name'])
print("Age: ", student['age'])

print("Course (using get()):", student.get('course'))
print("Course (with default):", student.get('course', 'Not Assigned'))

# ----------------------------------------------------------

# Q4: Check if key exists
#    Given:
#         car = {'brand' : 'BMW', 'model' : 'Alpina-XB7',
#                   'year' : 2026 }
#    Check:
#    - Is 'brand' in dictionary?
#    - Is 'color' in dictionary?
#    - Is 'model' not in dictionary?
#    Use 'in' and 'not in' operators

print("\n--- Q4: Key Membership ---")

car = {'brand' : 'BMW', 'model' : 'Alpina-XB7', 'year' : 2026 }
print("Car: ", car)

print("'brand' in car: ", 'brand' in car)
print("'color' in car: ", 'color' in car)
print("'model' not in car: ", 'model' not in car)

# ----------------------------------------------------------

# ==========================================================
# PART C:   Modifying Dictionaries
# ==========================================================

# Q5: Modify dictionary values
#    Given: 
#         product = {'name' : 'Laptop', 'price' : 10000, 
#                      'stock' : 10}
#    Modify:
#    - Change price to 9999
#    - Increase stock by 5
#    - Add new key 'discount' with value 10
#    Print dictionary after each change 

print("\n--- Q5: Modifying Values ---")

product = {'name' : 'Laptop', 'price' : 10000, 'stock' : 10}
print("Original: ", product)

product['price'] = 9999
print("After stock update: ", product)

product['stock'] = product['stock'] + 5
print("After stock update: ", product)

product['discount'] = 10
print("After adding discount: ", product)

# ----------------------------------------------------------