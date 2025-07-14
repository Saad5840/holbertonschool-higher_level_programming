# task_04_db.py
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [
                {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                } for row in reader
            ]
    except (FileNotFoundError, ValueError):
        return []

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            } for row in rows
        ]
    except sqlite3.Error:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        return render_template('items.html', items=data.get('items', []))
    except (FileNotFoundError, json.JSONDecodeError):
        return render_template('items.html', items=[])

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    products = (
        read_json('products.json') if source == 'json' else
        read_csv('products.csv') if source == 'csv' else
        read_sql()
    )
    
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
