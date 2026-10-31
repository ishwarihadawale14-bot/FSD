from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    students = [
        ["Ishwari",85],
        ["siddhi",45],
        ["Samruddhi",70],
        ["Sakshi",55],
        ["Sweta",65]
    ]

    result = [f"{s[0]} - {s[1]}" for s in students if s[1] > 60]

    return "<h2>Students Above 60</h2>" + "<br>".join(result)

app.run(debug=True)