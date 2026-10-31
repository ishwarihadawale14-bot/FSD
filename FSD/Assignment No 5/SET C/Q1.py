from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin":
            result = "Login Successful"
        else:
            result = "Invalid Username"
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Form</title>
    </head>
    <body>
        <h2>Login Form</h2>
        <form method="POST">
            Username:
            <input type="text" name="username">
            <br><br>

            Password:
            <input type="password" name="password">
            <br><br>
            <input type="submit" value="Login">

        </form>
        <h3>{result}</h3>

    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)
