from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('q2.html')
@app.route('/display',methods=['GET','POST'])
def display():
    if request.method=='POST':
        n=request.form.get('name')
        return f'Name: {n}'
app.run(debug=True)