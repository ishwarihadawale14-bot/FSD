from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {"id": 1, "title": "Jawan"},
    {"id": 2, "title": "Avengers"}
]

@app.route('/movies', methods=['GET'])
def home():
    return jsonify(movies)


@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    for movie in movies:
        if movie['id'] == id:
            return jsonify(movie)

    # Only return 404 after checking all movies
    return jsonify({
        "MSG": "MOVIE NOT FOUND"
    }), 404


app.run(debug=True)
