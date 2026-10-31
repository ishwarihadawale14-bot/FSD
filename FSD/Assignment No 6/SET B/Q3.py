from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    products = {
        "Computer":55000,
        "Mobile":25000,
        "Tablet":30000,
        "Watch":10000
    }

    p = max(products, key=products.get)

    return f"<h2>Most Expensive Product</h2>{p} = ₹{products[p]}"

app.run(debug=True)