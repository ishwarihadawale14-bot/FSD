from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    name = ""
    rating = ""
    comments = ""

    if request.method == "POST":

        name = request.form["name"]
        rating = request.form["rating"]
        comments = request.form["comments"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feedback Form</title>
    </head>
    <body>
        <h2>Feedback Form</h2>
        <form method="POST">
            Name:
            <input type="text" name="name"><br><br>
            Rating:
            <select name="rating">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select>
            <br><br>
            Comments:<br>
            <textarea name="comments"></textarea>
            <br><br>

            <input type="submit" value="Submit Feedback">
        </form>
        <h3>Submitted Feedback</h3>
        Name: {name}<br>
        Rating: {rating}/5<br>
        Comments: {comments}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
