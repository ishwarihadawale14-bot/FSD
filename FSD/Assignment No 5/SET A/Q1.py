from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""

    if request.method == "POST":
        name = request.form["name"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Name</title>
    </head>
    <body>

        <h2>Student Name</h2>

        <form method="POST">
            Enter Student Name:
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>

        <h3>Student Name: {name}</h3>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)