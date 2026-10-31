from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])

        result = num1 + num2

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Addition</title>
    </head>
    <body>

        <h2>Addition of Two Numbers</h2>

        <form method="POST">

            Enter First Number:
            <input type="number" name="num1"><br><br>

            Enter Second Number:
            <input type="number" name="num2"><br><br>

            <input type="submit" value="Add">

        </form>

        <h3>Addition = {result}</h3>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
