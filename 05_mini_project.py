"""

===========================================================
   LECTURE 04 - SET 05 :     MINI PROJECT
   Topics :    Dictionaries & Sets with Methods
============================================================

"""

# ==========================================================
#              SHOPPING CART AND INVENTORY
# ==========================================================

# ----------------------------------------------------------
#    STEP 01:     Product Details 
# ----------------------------------------------------------

print("\n--- Product Details ---")

product = {'name' : 'Laptop', 'price' : 9999, 'stock' : 10}
print("Product: ", product)

# Safe reading, modifying, updating, and property checking
print("Name: ", product.get('name'), "| Color: ", product.get('color', 'N/A'))

