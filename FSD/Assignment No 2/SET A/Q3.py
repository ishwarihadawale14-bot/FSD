from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/product', methods=[ 'GET' , 'POST'])
def product():
    if request.method == 'POST':
        a = int(request.form.get('fst'))
        b = int(request.form.get('snd'))
        return f'The product of {a} and {b} is: {a * b}'
app.run(debug=True)

