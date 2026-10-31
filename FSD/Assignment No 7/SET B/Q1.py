from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 25000},
    {"name": "Tablet", "price": 30000}
]

@app.route("/products", methods=["GET"])
def getproducts():
    return jsonify(products)

@app.route("/addproduct", methods=["POST"])
def addproduct():
    data = request.get_json()

    product = {
        "name": data["name"],
        "price": data["price"]
    }

    products.append(product)

    return jsonify(product)

app.run(debug=True)