from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return f"""
        <h1>Welcome to Flask</h1>
        """
app.run(debug=True)