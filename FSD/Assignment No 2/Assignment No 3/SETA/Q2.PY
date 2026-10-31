from flask import Flask, render_template_string

app = Flask(__name__)

# HTML code integrated inside the Python file
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Welcome to my Flask application!</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
