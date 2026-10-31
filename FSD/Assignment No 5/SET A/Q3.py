from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    area = ""

    if request.method == "POST":
        length = float(request.form["length"])
        breadth = float(request.form["breadth"])

        area = length * breadth

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rectangle Area</title>
    </head>
    <body>

        <h2>Area of Rectangle</h2>

        <form method="POST">

            Enter Length:
            <input type="number" name="length"><br><br>

            Enter Breadth:
            <input type="number" name="breadth"><br><br>

            <input type="submit" value="Calculate Area">

        </form>

        <h3>Area of Rectangle = {area}</h3>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)