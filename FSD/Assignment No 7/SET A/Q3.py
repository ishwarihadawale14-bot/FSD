from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/product", methods=["GET"])
def product():
    return jsonify({
        "name": "Laptop",
        "price": 50000,
        "category": "Electronics"
    })

app.run(debug=True)