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


Steps to run application:

### 1. Clone the repository
```bash
git clone https://github.com/anushri-patil/L7-informatics
cd L7_informatics
```

### 2. Create a virtual environment:
```bash
python -m venv venv
```

### 3. Activate the virtual environment
For Windows:
```bash
venv\Scripts\activate
```

### 4. Install the requirements
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
Set up the database by applying the migrations:
```bash
python manage.py migrate
```

### 6. Run the application
Start the development server:
```bash
python manage.py runserver
```

### 7. Access the application
Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.






