# 🛍️ Online Sales Analysis

This repository contains the solution for the **Final Project Assignment: Working with GitHub and Python**. The application simulates a basic inventory system with product management and cart functionality.

---

## 📦 `product.py`

Defines the `Product` class:
- **Attributes**:
  - `name`: Product name
  - `price`: Product price
  - `quantity`: Product quantity in stock
- **Methods**:
  - `show_info()`: Shows product details
  - `update_quantity(quantity)`: Updates the product's quantity

---

## 📊 `product_manager.py`

Defines the `ProductManager` class:
- **Attributes**:
  - `products`: A list of `Product` instances
- **Methods**:
  - `add_product(product)`: Adds a product to inventory
  - `show_all_products()`: Displays all product details
  - `average()`: Calculates total value of all products
  - `remove_by_name(name)`: Remove products by their names.


---

## 🛒 `cart.py`

Defines the `Cart` class:
- **Attribute**:
  - `cart_items`: A list of selected products
- **Methods**:
  - `add_product(product)`: Adds a product to the cart
  - `total_value()`: Returns total cost of the cart
  - `show()`: Displays all items in the cart

---

## 🧪 `main.py`

- Creates instances of all main classes
- Adds sample products to simulate usage
- Displays total values and inventory overview

---

## 🚀 Getting Started

```bash
python main.py

📦 online_sales_analysis/
├── product.py
├── product_manager.py
├── cart.py
├── main.py
└── README.md
