# Chocolate House - Django Web Application

This is a Django web application for a fictional Chocolate House that manages seasonal flavors, ingredient inventory, and customer flavor suggestions using SQLite as the database.

## Features

### Seasonal Flavor Offerings
- Add, update, and view seasonal flavors.
- Flavor names must be unique.
- Both name and season are required fields.
- **Only admin can delete flavors**.

### Ingredient Inventory
- Add, update, and view ingredients in the inventory.
- Ingredient quantities must be non-negative.
- Ingredient names must be unique.
- **Only admin can delete ingredients**.

### Customer Flavor Suggestions
- Add and view customer suggestions for new flavors.
- If no allergy concern is provided, it defaults to "No allergy concerns."

