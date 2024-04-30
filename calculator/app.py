from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/calculator',methods=['post'])
def calculate():
    ops=request.form.get('operation')
    num1=request.form.get('num1',type=float)
    num2=request.form.get('num2',type=float)

    if ops =="add":
        result=num1+num2
    elif ops =="subtract":
        result=num1-num2
    elif ops =="multiply":
        result=num1*num2
    elif ops =="divide":
        result=num1/num2
    else:
        result="invalid operation"
    
    return render_template('index1.html',result=result)

if __name__== '__main__':
    app.run(debug=True)