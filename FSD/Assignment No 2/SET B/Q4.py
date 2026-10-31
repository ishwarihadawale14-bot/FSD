from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        n=request.form.get('name')
        p=request.form.get('pass')
        if n=="ved" and p=="ishwari123@":
            return f'''Login Successful'''
        else:
            return "INVALID REDENTIALS"
app.run(debug=True)
