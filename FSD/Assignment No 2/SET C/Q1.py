from flask import Flask, request

app = Flask(__name__)

students = ["ishwari", "samruddhi", "siddhi", "purva"]

@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":
        name = request.form.get("name")

        if name in students:
            result = f"Student found: {name}"
        else:
            result = f"Student not found: {name}"

        return f"""
        <h2>Search Result</h2>
        <p>{result}</p>
        <a href="/search">Search Again</a>
        """

    return """
    <h2>Student Search</h2>

    <form method="POST">
        Name:
        <input type="text" name="name">
        <input type="submit" value="Search">
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
