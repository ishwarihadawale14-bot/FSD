from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    name = ""
    emp_id = ""
    department = ""
    salary = ""

    if request.method == "POST":

        name = request.form["name"]
        emp_id = request.form["id"]
        department = request.form["department"]
        salary = request.form["salary"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee Details</title>
    </head>
    <body>

        <h2>Employee Details</h2>

        <form method="POST">

            Employee Name:
            <input type="text" name="name"><br><br>

            Employee ID:
            <input type="text" name="id"><br><br>

            Department:
            <input type="text" name="department"><br><br>

            Salary:
            <input type="number" name="salary"><br><br>

            <input type="submit" value="Submit">

        </form>

        <h3>Employee Information</h3>

        Employee Name: {name}<br>
        Employee ID: {emp_id}<br>
        Department: {department}<br>
        Salary: ₹{salary}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)