from flask import Flask,request,render_template
books=[{"bookname":"Wings of Fire","Price":1500,"Written by":"ISHUU"},
       {"bookname":"Psychology","Price":2800,"Written by":"ISHUU"},
       {"bookname":"Manipulation","Price":3000,"Written by":"ISHUU"},
       {"bookname":"Be valuable","Price":1800,"Written by":"ISHUU"},
       {"bookname":"Disrespect","Price":500,"Written by":"ISHUU"}]
app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('index2.html')
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
        bookname=request.form.get('bname')
        for book in books:
            if book['bookname']==bookname:
                return book
app.run(debug=True)