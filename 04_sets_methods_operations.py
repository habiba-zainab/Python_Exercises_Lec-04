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

my_set.update({8, 9})
print("After update({8, 9}): ", my_set)

# ----------------------------------------------------------

# Q2:  pop() and clear() methods
#    Given:    
#             numbers = {10, 20, 30, 40, 50} 
#    - Pop one element (random)
#    - Pop another element
#    - Show remaining set
#    - Clear the set

print("\n--- Q2: pop() & clear() ---")

numbers = {10, 20, 30, 40, 50}
print("Original: ", numbers)

popped1 = numbers.pop()
print("Popped: ", popped1, "(random element)")
print("Remaining: ", numbers)

popped2 = numbers.pop()
print("Popped: ", popped2)
print("Remaining: ", numbers)

numbers.clear()
print("After clear(): ", numbers)

# ----------------------------------------------------------

# Q3:  copy() method
#    Given: 
#            original = {1, 2, 3, 4, 5}
#    - Create copy
#    - Modify copy
#    - Show original is unchanged
#    - Show they are different objects

print("\n--- Q3: copy() method ---")

original = {1, 2, 3, 4, 5}
copy_set = original.copy()

print("Original: ", original)
print("Copy: ", copy_set)

copy_set.update({6, 7})
print("Modified copy: ", copy_set)
print("Original unchanged: ", original)
print("Are different objects: ", original is not copy_set)

# ----------------------------------------------------------

# ==========================================================
# PART B:   Core Mathematical Venn Operations
# ==========================================================

# Q4:  union() - Combine sets
#    Given:           
#                set_a = {1, 2, 3, 4}
#                set_b = {3, 4, 5, 6}
#                set_c = {5, 6, 7, 8}
#    Find union using: 
#    - union() method
#    - | operator
#    - Union of all three sets

print("\n--- Q4: union() ---")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7, 8}

print("Set A: ", set_a)
print("Set B: ", set_b)
print("Set C: ", set_c)

print("\nA union B (method): ", set_a.union(set_b))
print("A | B (operator): ", set_a | set_b)
print("A | B | C: ", set_a | set_b | set_c)

# ----------------------------------------------------------