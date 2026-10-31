from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    product = ""
    quantity = ""
    price = ""
    total = ""

    if request.method == "POST":

        product = request.form["product"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        total = quantity * price

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Product Order</title>
    </head>
    <body>

        <h2>Product Order Form</h2>

        <form method="POST">

            Product Name:
            <input type="text" name="product">
            <br><br>

            Quantity:
            <input type="number" name="quantity">
            <br><br>

            Price:
            <input type="number" name="price">
            <br><br>

            <input type="submit" value="Place Order">

        </form>

        <h3>Order Details</h3>

        Product Name: {product}<br>
        Quantity: {quantity}<br>
        Price: ₹{price}<br>
        Total Amount: ₹{total}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)