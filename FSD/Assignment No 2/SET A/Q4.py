from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index2.htm')
@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method=='POST':
        a=str(request.form.get('name'))
        b=str(request.form.get('fd'))
        return f'Thank you {a} for your feedback: "{b}"'
app.run(debug=True)