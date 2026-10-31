from flask import Flask,jsonify
app=Flask(__name__)
Movies=[
    {"id":1,"title":"jawan"},
    {"id":2,"title":"avengers"},
    {"id":3,"title":"3 idiots"}
]

@app.route('/' , methods=['GET'])
def home():
    return jsonify(Movies)
app.run(debug=True)
