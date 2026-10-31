from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = ""

    if request.method == "POST":
        m = [
            int(request.form["m1"]),
            int(request.form["m2"]),
            int(request.form["m3"]),
            int(request.form["m4"]),
            int(request.form["m5"])
        ]

        result = f"""
        Total: {sum(m)}<br>
        Average: {sum(m)/len(m)}<br>
        Highest: {max(m)}<br>
        Lowest: {min(m)}
        """

    return f"""
    <h2>Student Marks</h2>
    <form method="post">
    Mark 1: <input name="m1"><br><br>
    Mark 2: <input name="m2"><br><br>
    Mark 3: <input name="m3"><br><br>
    Mark 4: <input name="m4"><br><br>
    Mark 5: <input name="m5"><br><br>
    <input type="submit" value="Calculate">
    </form>
    <h3>{result}</h3>
    """

app.run(debug=True)