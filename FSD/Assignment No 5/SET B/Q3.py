from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    basic = ""
    allowance = 2000
    total = ""

    if request.method == "POST":

        basic = float(request.form["basic"])

        total = basic + allowance

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Salary Calculation</title>
    </head>
    <body>

        <h2>Employee Salary</h2>

        <form method="POST">

            Enter Basic Salary:
            <input type="number" name="basic">
            <br><br>

            <input type="submit" value="Calculate Salary">

        </form>

        <h3>Salary Details</h3>

        Basic Salary: ₹{basic}<br>
        Fixed Allowance: ₹{allowance}<br>
        Total Salary: ₹{total}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)