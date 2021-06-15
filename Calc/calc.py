#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

def add(left, right):
    return left + right 

def minus(left, right):
    return left - right 

def multiplication(left, right):
    return left * right 
   
def division(left, right):
    if right !=0:
        return left / right
    else:
        return 'division by zero \n'

def chek_data(value):
    if value != None:
        return True
    else:
        return False

def is_digit(num):
    if chek_data(num) and isinstance(num, int):
        return True
    else:
        return False
    
d_operator = {
  '+': add,
  '-': minus,
  '*': multiplication,
  '/': division
}

#d = {}

#def chek_operator(trans):
@app.route("/count_up", methods=["POST"])
def count_up():
    d = request.json    
    if is_digit(d.get('left', None)):
        if is_digit(d.get('right', None)):
            if chek_data(d.get('operator', None)) and chek_data(d_operator.get(d['operator'], None)):
                return str(d_operator[d['operator']](d['left'], d['right'])) + '\n'
            else:
                return 'invalid operator \n'
        else:
            return 'invalid operand "right" \n'
    else:
        return 'invalid operand "left"\n'
    
@app.route('/', methods=["POST"])
def help():
    print(request.json)
    return request.json

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)
