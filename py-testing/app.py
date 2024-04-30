from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route('/hello',methods=['GET'])
def hello():
    return jsonify(msg="HELLO WORLD")
@app.route('/add',methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get("number1")
    num2 = data.get("number2")
    if num1 is None or num2 is None:
        return jsonify(error="Invalid input"), 400
    if num1 is not int or num2 is not int:
        return jsonify(error="Invalid input"), 400
    result = num1 + num2
    return jsonify(result=result)

if __name__== '__main__':
    app.run(debug=True,port=8000)