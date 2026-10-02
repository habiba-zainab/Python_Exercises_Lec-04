"""

===========================================================
   LECTURE 04 - SET 03 : BASICS OF SETS
   Topics : Sets Basics - Creating, Properties, Uniqueness
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Set Creation & Properties
# ==========================================================

# Q1: Create different types of sets
#    Create:
#    - Empty set (use set(), not {})
#    - Set from list [1, 2, 3, 4, 5]
#    - Set from string  "hello"
#    - Set with mixed types
#    - Set from range(1, 10)
#    Print each and show length

print("\n--- Q1: Creating Sets ---")

empty = set()
from_list = set([1, 2, 3, 4, 5])
from_string = set("hello")
mixed = {1, "World", 66.5, True}
from_range = set(range(1, 10))

print("Empty: ", empty, "(Length: ", len(empty), ")")
print("From list: ", from_list, "(Length: ", len(from_list), ")")
print("From string: ", from_string, "(Length: ", len(from_string), ")")
print("Mixed: ", mixed, "(Length: ", len(mixed), ")")
print("From range: ", from_range, "(Length: ", len(range), ")")

# ----------------------------------------------------------

# Q2: Sets are unordered
#    Create same set multiple times:
#    set1 = {5, 2, 8, 1, 9}
#    set2 = {1, 2, 5, 8, 9}
#    Show they are equal even though order is different 

print("\n--- Q2: Unordered Nature ---")

set1 = {5, 2, 8, 1, 9}
set2 = {1, 2, 5, 8, 9}

print("set1: ", set1)
print("set2: ", set2)
print("Are equal: ", set1 == set2)

# ----------------------------------------------------------

# Q3: Set length and min/max
#    Given:   
#            numbers = {45, 12, 78, 23, 67, 89, 34, 56}
#    Find:
#    - Length of set
#    - Minimum number
#    - Maximum number
#    - Sum of all nuumbers
#    - Average

print("\n--- Q3: Set Statistics ---")

numbers = {45, 12, 78, 23, 67, 89, 34, 56}

print("Numbers: ", numbers)
print("Length: ", len(numbers))
print("Minimum: ", min(numbers))
print("Maximum: ", max(numbers))
print("Sum: ", sum(numbers))
print("Average: ", sum(numbers) / len(numbers))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Uniqueness & Deduplication
# ==========================================================

# Q4: Sets remove duplicates automatically
#    Given: 
#           numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
#    Convert to set to remove duplicates
#    Compare original length vs set length
#    Convert back to sorted list

print("\n--- Q4: Remove Duplicates ---")

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print("Original list: ", numbers)
print("Length: ", len(numbers))

unique_set = set(numbers)
print("As set: ", unique_set)
print("Length: ", len(unique_set))
print("Duplicate removed: ", len(numbers) - len(unique_set))

sorted_list = sorted(list(unique_set))
print("Back to sorted list: ", sorted_list)

# ----------------------------------------------------------

# Q5: Find unique characters in string
#    Given:      text = "programming"
#    Find all unique characters
#    Count total vs unique characters
#    Show characters in sorted order

print("\n--- Q5: Unique Characters ---")

text = "programming"
print("Text: ", repr(text))
print("Total characters: ", len(text))

unique_chars = set(text)
print("Unique characters: ", unique_chars)
print("Unique count: ", unique_chars)
print("Sorted: ", sorted(unique_chars))

# ----------------------------------------------------------

# ==========================================================
# PART C:   Set Membership Testing & Type Conversion
# ==========================================================

# Q6:  Set membership testing
#    Given: 
#            fruits = {'apple', 'banana', 'cherry', 'date'}
#    Check: 
#    - Is 'apple' in set?
#    - Is 'mango' in set?
#    - Is 'banana' not in set?
#    Show that membership testing is very fast in sets

print("\n--- Q6: Membership Testing ---")

fruits = {'apple', 'banana', 'cherry', 'date'}

print("Fruits: ", fruits)
print("'apple' in fruits: ", 'apple' in fruits)
print("'mango' in fruits: ", 'mango' in fruits)
print("'banana' not in fruits: ", 'banana' not in fruits)

# ----------------------------------------------------------