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

product['price'] = 8999
product.update({'stock' : 15, 'brand' : 'hp'})
print("Updated Product: ", product)

print("Keys: ", list(product.keys()), "| Values: ", list(product.values()))
print("Total Keys: ", len(product), "| Popped Brand: ", product.pop('brand'))

# ----------------------------------------------------------
#    STEP 02:     Inventory Database 
# ----------------------------------------------------------

print("\n--- Inventory Database ---")

inventory = {
    'P01' : {'name' : 'Laptop', 'price' : 9999},
    'P02' : {'name' : 'Mouse', 'price' : 250}
}

# Accessing and modifying nested dictionaries
print("Laptop Price: ", inventory['P01']['price'])

inventory['P01']['stock'] = 10
print("Updated Laptop Info: ", inventory['P01'])

# Find most expensive item using max() with key parameter
top = max(inventory.items(), key=lambda x: x[1]['price'])
print("Most Expensive Item ID: ", top[0])

# Direct generation and default stock generation
print("Squares Tables: ", {1 : 1, 2 : 4, 3 : 9})
print("Default Inventory Stock: ", dict.fromkeys(['P01', 'P02'], 0))

# ----------------------------------------------------------
#    STEP 03:     Cart Selection 
# ----------------------------------------------------------

print("\n--- Cart Selection ---")

cart = {'Laptop', 'Mouse'}
wishlist = {'Keyboard', 'Monitor', 'Mouse'}
print("Cart: ", cart, "| Wishlist: ", wishlist)

# Membership testing
print("Is 'Mouse' in cart? ", 'Mouse' in cart)

# Adding and updating items
cart.add('keyboard')
cart.update(['Monitor'])
print("After Add & Upddate: ", cart)

# Safe removal (discard) and direct removal (remove)
cart.discard('Monitor')
cart.remove('Laptop')
print("After Discard & Remove: ", cart)
