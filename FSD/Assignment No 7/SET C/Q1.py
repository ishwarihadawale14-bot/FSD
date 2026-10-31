from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/result", methods=["GET"])
def result():
    return jsonify({
        "name": "Ishwari",
        "marks": 80,
        "result": "Pass"
    })
@app.route("/addresult", methods=["POST"])
def addresult():
    data = request.get_json()
    name = data["name"]
    marks = data["marks"]
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"
    return jsonify({
        "name": name,
        "marks": marks,
        "result": result
    })
app.run(debug=True)