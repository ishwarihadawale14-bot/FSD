from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('a.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        n=request.form.get('name')
        a=request.form.get('age')
        p=request.form.get('project')
        c=request.form.get('class')
        return f'Name: {n} <br> Age: {a} <br> Project Name: {p} <br> Class: {c}'
app.run(debug=True)