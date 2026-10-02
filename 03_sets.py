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
#    Show they arre equal even though order is different 
#    Show that sets don't support indexing
