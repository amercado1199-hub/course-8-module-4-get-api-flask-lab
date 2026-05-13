from flask import Flask, jsonify, request

app = Flask(__name__)

#Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Book", "price": 9.99, "category": "Books"},
    {"id": 3, "name": "Headphones", "price": 199.99, "category": "Audio"}
]

#Homepage route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API!"})

#Get all products or filter by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered_products = [product for product in products if product["category"].lower() == category.lower()]
        return jsonify(filtered_products)
    return jsonify(products)

#Get a product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)