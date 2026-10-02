"""

===========================================================
   LECTURE 04 - SET 04 : SETS METHODS & OPERATIONS
   Topics :    Sets Methods & Mathematical Operation
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Basic Set Modifications
# ==========================================================

# Q1:  add() and update() methods
#    Start with:    my_set = {1, 2, 3}
#    - Add element 4 using add()
#    - Add element 2 (already exists, no change)
#    - Add multiple elements using update([5, 6, 7])
#    - Update with another set {8, 9}

print("\n--- Q1: add() & update() ---")

my_set = {1, 2, 3}
print("Start: ", my_set)

my_set.add(4)
print("After add(4): ", my_set)

my_set.add(2)
print("After add(2): ", my_set, "(no change)")

my_set.update([5, 6, 7])
print("After update([5, 6, 7]): ", my_set)
