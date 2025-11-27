from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
DB_NAME = "ecommerce.db"

def init_db():
    """Create database tables if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            category TEXT,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            total_price REAL NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized!")

# Initialize database when app starts
init_db()

# ===== API ROUTES (Layer C) =====

@app.route("/", methods=["GET"])
def home():
    """Welcome endpoint"""
    return jsonify({"message": "Welcome to E-Commerce API"})

@app.route("/products", methods=["GET"])
def get_all_products():
    """Get all products"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, stock, category FROM products")
        products = cursor.fetchall()
        conn.close()
        
        result = [
            {"id": p[0], "name": p[1], "price": p[2], "stock": p[3], "category": p[4]}
            for p in products
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/products", methods=["POST"])
def add_product():
    """Add a new product"""
    try:
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        stock = data.get("stock")
        category = data.get("category")
        
        if not name or not price or not stock:
            return jsonify({"error": "Missing required fields"}), 400
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, stock, category) VALUES (?, ?, ?, ?)",
            (name, price, stock, category)
        )
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update an existing product"""
    try:
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        stock = data.get("stock")
        category = data.get("category")
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name=?, price=?, stock=?, category=? WHERE id=?",
            (name, price, stock, category, product_id)
        )
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a product"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)